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
    # product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    products_order = profile.orders.all()
    # has_plan = profile.has_plan
    nutrition_price = None
    
    for o in products_order:
        # print(order.order_number)
        for p in o.lineorders.all():
            get_cat = p.product.category.category_name 
            total_items = order.order_total
            product_name = p.product.product_name
            # print(product_name)
           
            if get_cat == 'nutrition_plan':
                nutrition_price = p.product.price
                product_name = p.product.product_name

        if total_items < settings.FREE_DELIVERY:
            if total_items == nutrition_price and get_cat == 'nutrition_plan':
                print(get_cat)
                delivery_cost = 0
                print('IF')
            elif get_cat == 'nutrition_plan' and product_name:
                delivery_cost = (total_items - nutrition_price) * Decimal(settings.DELIVERY_PERCENTAGE / 100)
                print('ELIF')
            else:
                if product_name != product_name:
                    print('IF ELSE')
                    delivery_cost = (total_items - nutrition_price) * Decimal(settings.DELIVERY_PERCENTAGE / 100)
                    
                else:
                    print('ELSE ELSE')
                    delivery_cost = total_items * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        else:
            print('LAST ELSE')
            delivery_cost = 0

        grand_total = delivery_cost + total_items

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the purchase date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'products_order': products_order,
        'delivery_cost': delivery_cost,
        'total_items': total_items,
        'grand_total': grand_total,
        'from_user_profile': True,
    }

    return render(request, template, context)
