from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import AddProductForm


def shop_all_products(request):
    """ A view to show all products, including sorting and search queries """

    shop_products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                shop_products = shop_products.annotate(lower_name=Lower('product_name'))
            if sort_key == 'category':
                sort_key = 'category__category_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            shop_products = shop_products.order_by(sort_key) 

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            shop_products = shop_products.filter(category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('shop_products'))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            shop_products = shop_products.filter(queries)

    selected_sorting = f'{sort}_{direction}'

    context = {
        'products': shop_products,
        'search_term': query,
        'selected_categories': categories,
        'selected_sorting': selected_sorting,
    }

    return render(request, 'products/products.html', context)


def get_product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product_admin(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission to add products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('get_product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed! Please ensure you added the products correctly!')
    else:
        form = AddProductForm()

    template = 'products/add_product_admin.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product_admin(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission to edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('get_product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = AddProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')

    template = 'products/edit_product_admin.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product_admin(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission to delete products.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product is deleted!')
    return redirect(reverse('shop_products'))