from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import ProductOrderForm
from shop_bag.contexts import bag_products

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shop_bag = request.session.get('shop_bag', {})
    if not shop_bag:
        messages.error(request, "There are no products at your shopping bag!")
        return redirect(reverse('shop_products'))

    current_bag = bag_products(request)
    total_bag = current_bag['shop_total']
    stripe_total = round(total_bag * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    product_order_form = ProductOrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Is it set in your environment variables?')

    template = 'checkout/checkout.html'
    context = {
        'product_order_form':product_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)