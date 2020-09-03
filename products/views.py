from django.shortcuts import render
from .models import Product

# Create your views here.


def shop_all_products(request):
    """ A view to show all products, including sorting and search queries """

    shop_products = Product.objects.all()

    context = {
        'products': shop_products,
    }

    return render(request, 'products/products.html', context)
