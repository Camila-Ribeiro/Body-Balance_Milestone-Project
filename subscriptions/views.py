from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Plan
from .forms import AddPlanForm

from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

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