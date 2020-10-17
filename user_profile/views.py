from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from nutrition.views import nutrition
from checkout.models import ProductOrder
from .models import UserProfile
from .forms import UserProfileForm


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


def product_order_history(request, order_number):
    order = get_object_or_404(ProductOrder, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_user_profile': True,
    }

    return render(request, template, context)
