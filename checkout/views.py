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
        'stripe_public_key':'pk_test_51HPVMQEcvV2absiRNu1nkSZkj1qcnM4LAaNp2z1GMOPSZH0zGbtX2UuWIr5Ze1cs2kwHjQ4QA6qNOAdy830Y0RLX00ygGPN2eq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)