from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Plan
from .forms import AddPlanForm


def shop_subscription_plan(request):
    """ A view to show all subscription plans available to purchase """

    subscriptions = Plan.objects.all()

    context = {
        'subscriptions': subscriptions,
    }
    return render(request, 'subscriptions/subscriptions.html', context)


@login_required
def add_plan_admin(request):
    """ Add a subscription plan available to purchase """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission to add Subscription Plans.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddPlanForm(request.POST, request.FILES)
        if form.is_valid():
            subscription_plan = form.save()
            messages.success(request, 'Subscription Plan added successfully!')
            return redirect(reverse('shop_subscription_plan'))
        else:
            messages.error(request, 'Failed! Please ensure you added the Subscription Plan correctly!')
    else:
        form = AddPlanForm()

    template = 'subscriptions/add_plan_admin.html'
    context = {
        'form': form,
    }

    return render(request, template, context)