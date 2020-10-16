from django.shortcuts import render, redirect, reverse, HttpResponse,\
                             get_object_or_404
from django.contrib import messages

from products.models import Product


def shop_bag(request):
    """ A view that renders the shopping bag page """
    return render(request, 'shop_bag/shop-bag.html')


def add_products_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    shop_product = get_object_or_404(Product, pk=product_id)
    product_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shop_bag = request.session.get('shop_bag', {})

    if size:
        if product_id in list(shop_bag.keys()):
            if size in shop_bag[product_id]['items_by_size'].keys():
                shop_bag[product_id]['items_by_size'][size] += product_quantity
                messages.success(request, f'Updated size {size.upper()}\
                    {shop_product.product_name} quantity to\
                        {shop_bag[product_id]["items_by_size"][size]}')
            else:
                shop_bag[product_id]['items_by_size'][size] = product_quantity
                messages.success(request, f'Added size\
                    {size.upper()} {shop_product.product_name} to your bag')
        else:
            shop_bag[product_id] = {'items_by_size': {size: product_quantity}}
            messages.success(request, f'Added size\
                {size.upper()}, {shop_product.product_name} to your bag')
    else:
        if product_id in list(shop_bag.keys()):
            shop_bag[product_id] += product_quantity
            messages.success(request, f'{shop_product.product_name}\
                quantity is updated to {shop_bag[product_id]}!')
        else:
            shop_bag[product_id] = product_quantity
            messages.success(request, f'\
                {shop_product.product_name} is added to your bag!')

    request.session['shop_bag'] = shop_bag
    return redirect(redirect_url)


def update_quantity_bag(request, product_id):
    """Update the quantity of the specified product to the specified amount"""

    shop_product = get_object_or_404(Product, pk=product_id)
    product_quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shop_bag = request.session.get('shop_bag', {})

    if size:
        if product_quantity > 0:
            shop_bag[product_id]['items_by_size'][size] = product_quantity
            messages.success(request, f'Product:\
                {shop_product.product_name}, Size: {size.upper()},\
                    Quantity: {shop_bag[product_id]["items_by_size"][size]}')
        else:
            del shop_bag[product_id]['items_by_size'][size]
            if not shop_bag[product_id]['items_by_size']:
                shop_bag.pop(product_id)
            messages.success(request, f'Product:\
                {shop_product.product_name},\
                    Size: {size.upper()} is removed from your bag')
    else:
        if product_quantity > 0:
            shop_bag[product_id] = product_quantity
            messages.success(request, f'Updated {shop_product.product_name}\
                quantity to {shop_bag[product_id]}')
        else:
            shop_bag.pop(product_id)
            messages.success(request, f'{shop_product.product_name}\
                is removed from your bag')

    request.session['shop_bag'] = shop_bag
    return redirect(reverse('shop_bag'))


def remove_product(request, product_id):
    """Remove the product from the shopping bag"""

    try:
        shop_product = get_object_or_404(Product, pk=product_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shop_bag = request.session.get('shop_bag', {})

        if size:
            del shop_bag[product_id]['items_by_size'][size]
            if not shop_bag[product_id]['items_by_size']:
                shop_bag.pop(product_id)
            messages.success(request, f'Product: {shop_product.product_name},\
                Size: {size.upper()} is removed from your bag')

        else:
            shop_bag.pop(product_id)
            messages.success(request, f'{shop_product.product_name}\
                is removed from your bag')

        request.session['shop_bag'] = shop_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
