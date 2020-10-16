from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.views import check_user
from .models import Plan
from .forms import AddPlanForm


def shop_subscription_plan(request):
    """ A view to show all subscription plans available to purchase """
    subscriptions = Plan.objects.all()
    has_plan = check_user(request)

    context = {
        'subscriptions': subscriptions,
        'has_plan': has_plan,
    }
    return render(request, 'subscriptions/subscriptions.html', context)


def get_plan_id(request, plan_id):
    plan_id = get_object_or_404(Plan, pk=plan_id)
    print(plan_id)
    context = {
        'plan_id': plan_id,
    }

    return render(request, 'subscriptions/edit_subscription_admin.html',
                  context)


@login_required
def edit_subscription_admin(request, plan_id):
    """ Edit a subscription plan  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission \
        to edit the subscription plan.')
        return redirect(reverse('home'))

    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        print(plan)
        form = AddPlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated plan!')
            return redirect('shop_subscription_plan')
        else:
            messages.error(request, 'Failed to update plan. Please ensure the \
            form is valid.')
    else:
        form = AddPlanForm(instance=plan)
        messages.info(request, f'You are editing {plan.plan_duration}')

    template = 'subscriptions/edit_subscription_admin.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)
