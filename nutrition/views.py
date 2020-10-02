from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from subscriptions.views import is_not_anonymous

from checkout.models import SubscriptionOrder
from user_profile.models import UserProfile
from .models import Nutrition

from .forms import AddNutritionPlanForm


def nutrition(request):
    nutrition_obj = Nutrition.objects.all()
    subscription_order = SubscriptionOrder.objects.all()
    user_has_order = is_not_anonymous(request)

    if user_has_order != 'anonymous' and user_has_order != 'no-subscribed':
        template = 'nutrition/nutrition.html'
    else:
        return redirect(reverse('shop_subscription_plan'))

    context = {
        'nutrition_obj': nutrition_obj,
    }

    return render(request, template, context)


@login_required
def add_menu_admin(request):
    """ Add a nutrition plan available to purchase """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission to add Nutrition Details.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddNutritionPlanForm(request.POST, request.FILES)
        if form.is_valid():
            nutrition_plan = form.save()
            messages.success(request, 'Nutrition Plan added successfully!')
            return redirect(reverse('shop_nutrition_plan'))
        else:
            messages.error(request, 'Failed! Please ensure you added the Nutrition Plan correctly!')
    else:
        form = AddNutritionPlanForm()

    template = 'nutrition/add_menu_admin.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
