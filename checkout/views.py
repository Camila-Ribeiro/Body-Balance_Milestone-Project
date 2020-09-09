from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ProductOrderForm

# Create your views here.


def checkout(request):
    shop_bag = request.session.get('shop_bag', {})
    if not shop_bag:
        messages.error(request, "There are no products at your shopping bag!")
        return redirect(reverse('shop_products'))

    product_order_form = ProductOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'product_order_form':product_order_form,
    }

    return render(request, template, context)