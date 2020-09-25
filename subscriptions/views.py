from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import stripe

from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile
from .models import Plan
from checkout.models import SubscriptionOrder

from .forms import AddPlanForm, SubscriptionOrderForm

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt



stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET_SUB


def shop_subscription_plan(request):
    """ A view to show all subscription plans available to purchase """

    subscriptions = Plan.objects.all()

    context = {
        'subscriptions': subscriptions,
    }
    return render(request, 'subscriptions/subscriptions.html', context)

def thanks(request):
    return render(request, 'subscriptions/thanks.html')


@csrf_exempt
def checkout_plan(request):

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            # plan = Plan.objects.get(plan_name=plan_name)
            order_form = SubscriptionOrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                # 'plan_name': plan.plan_name,
            })
            print(order_form)
        except UserProfile.DoesNotExist:
            order_form = SubscriptionOrderForm()
    else:
        order_form = SubscriptionOrderForm()


    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HUY3FEcvV2absiRjrCdirZO',
            'quantity': 1,
        }],
        mode='payment',
       success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('shop_subscription_plan')),
    )

    return JsonResponse({
        # 'order_form':order_form,
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })
   


 
@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    # endpoint_secret = 'settings.STRIPE_WEBHOOK_SECRET_SUB'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)


def get_plan_id(request, plan_id):

    plan_id = get_object_or_404(Plan, pk=plan_id)
    print(plan_id)
    context = {
        'plan_id': plan_id,
    }

    return render(request, 'subscriptions/edit_plan_admin.html', context)


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
            return redirect(reverse('get_plan_id', args=[plan.id]))
        else:
            messages.error(request, 'Failed! Please ensure you added the Subscription Plan correctly!')
    else:
        form = AddPlanForm()

    template = 'subscriptions/add_plan_admin.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_plan_admin(request, plan_id):
    """ Edit a subscription plan  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have the permission to edit the subscription plan.')
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
            messages.error(request, 'Failed to upda§te plan. Please ensure the form is valid.')
    else:
        form = AddPlanForm(instance=plan)
        messages.info(request, f'You are editing {plan.plan_name}')

    template = 'subscriptions/edit_plan_admin.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)


