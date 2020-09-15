from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import ProductOrderForm
from .models import ProductOrder, ProductLineOrder
from products.models import Product
from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile
from shop_bag.contexts import bag_products

import stripe
import json

# Create your views here.


@require_POST
def cache_checkout(request):
    try:
        pay_intent_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pay_intent_id, 
            metadata={
                'shop_bag': json.dumps(request.session.get('shop_bag', {})),
                'save_user_info': request.POST.get('save_info_box'),
                'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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
            order = order_form.save(commit=False)
            pay_intent_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pay_intent_id
            order.original_shop_bag = json.dumps(shop_bag)
            order.save()
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
                                product_quantity=product_quantity,
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
            request.session['save_user_info'] = 'save-info_box' in request.POST
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

         # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = ProductOrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = ProductOrderForm()
        else:
            order_form = ProductOrderForm()


    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Is it set in your environment variables?')

    template = 'checkout/checkout.html'
    context = {
        'order_form':order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_user_info = request.session.get('save_user_info')
    order = get_object_or_404(ProductOrder, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_user_info:
            user_profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(user_profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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