from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from nutrition.views import nutrition
from checkout.models import ProductOrder
from .models import UserProfile
from .forms import UserProfileForm
from django.conf import settings
from products.models import Product



@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'User profile updated successfully!')
        else:
            messages.error(request, 'Failed. Please ensure you updated the\
                form correctly!')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # call nutrition func from nutrition.views
    nutrition(request)

    template = 'user_profile/user-profile.html'

    context = {
        'form': form,
        'orders': orders,
        'on_user_profile_page': True
    }

    return render(request, template, context)


def nutrition_delivery():
    """Convert value to Decimal keeping the given number of digits after the
    leading number."""

    subtract_delivery = 2.99
    get_float = float(subtract_delivery)
    convert_to_decimal = Decimal(get_float).quantize(Decimal('1.00'))
    return convert_to_decimal


def product_order_history(request, order_number):
    order = get_object_or_404(ProductOrder, order_number=order_number)
    profile = get_object_or_404(UserProfile, user=request.user)
    products_order = profile.orders.all()
    nut_delivery = nutrition_delivery()

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the purchase date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'products_order': products_order,
        'nut_delivery': nut_delivery,
        'from_user_profile': True,
    }

    return render(request, template, context)
