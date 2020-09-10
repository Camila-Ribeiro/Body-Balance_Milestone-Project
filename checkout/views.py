from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import ProductOrderForm
from .models import ProductOrder, ProductLineOrder
from products.models import Product
from shop_bag.contexts import bag_products

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shop_bag = request.session.get('shop_bag', {})

        form_database = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = ProductOrderForm(form_database)
        if order_form.is_valid():
            order = order_form.save()
            for product_id, item_data in shop_bag.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(item_data, int):
                        product_line_order = ProductLineOrder(
                            order=order,
                            product=product,
                            product_quantity=item_data,
                        )
                        product_line_order.save()
                    else:
                        for size, product_quantity in item_data['items_by_size'].items():
                            product_line_order = ProductLineOrder(
                                order=order,
                                product=product,
                                product_quantity=quantity,
                                product_size=size,
                            )
                            product_line_order.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "There is a product in your shop bag that bag wasn't found in our database. "
                        "Please get in contact with us for further assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shop_bag'))
            request.session['save_order_info'] = 'save-order-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Error! \
            Please double check your information.')
    else:
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_order_info = request.session.get('save_order_info')
    order = get_object_or_404(ProductOrder, order_number=order_number)
    messages.success(request, f'Your order was successfully processed! \
        The order number is {order_number}. A confirmation \
        email will be sent to {order.email} shortly.')

    if 'shop_bag' in request.session:
        del request.session['shop_bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)