from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from checkout.webhook_handler import StripeWebhookHandler

import stripe

from user_profile.models import UserProfile
from checkout.models import SubscriptionOrder
from .models import Plan
from .forms import AddPlanForm, SubscriptionOrderForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET


def is_not_anonymous(request):
    if request.user.is_authenticated:
        subscription_order = SubscriptionOrder.objects.all()
        online_user = UserProfile.objects.get(user=request.user)

        for user in subscription_order:
            if online_user != user.user_profile:
                return('no-subscribed')
            else:
                return filter_user_has_order(user.user_profile, subscription_order)
    else:
        return('anonymous')

def shop_subscription_plan(request):
    """ A view to show all subscription plans available to purchase """
    subscriptions = Plan.objects.all()
    subscription_order = SubscriptionOrder.objects.all()

    user_has_order = is_not_anonymous(request)

    context = {
        'subscriptions': subscriptions,
        'subscription_order': subscription_order,
        'user_has_order': user_has_order,
    }
    return render(request, 'subscriptions/subscriptions.html', context)


def thanks(request):
    # stripe_session = stripe_webhook(request)
    print(request)
    # if request.user.is_authenticated:
    #     subscription_order = SubscriptionOrder.objects.all()
    #     profile = UserProfile.objects.get(user=request.user)
    #     has_order = filter_user_has_order(profile, subscription_order)

    #     form_database_sub = {
    #         'full_name': profile,
    #         'email': profile.user.email,
    #         'user_profile': profile
    #     }

    #     order_form_ = SubscriptionOrderForm(form_database_sub)

    #     print(has_order)

    #     if order_form_.is_valid() and has_order is None:
    #         order_form_ = order_form_.save(commit=False)
    #         pay_intent_id = stripe.api_key.split('_secret')[0]
    #         order_form_.stripe_pid = pay_intent_id
    #         order_form_.save()
    #         subscription_order_last = SubscriptionOrder.objects.latest('order_number')
    #         template = 'subscriptions/thanks.html'
    #     else:
    #         return redirect(reverse('shop_subscription_plan'))
    
    context = {
        # 'subscription_order': subscription_order_last,
        # 'has_order': has_order,
        # 'from_user_profile': True,
    }

    return render(request, 'subscriptions/thanks.html', context)



@csrf_exempt
def checkout_plan(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HYucdEcvV2absiRYT8BZha0',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('shop_subscription_plan')),
    )

    return JsonResponse({
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


# @require_POST
# @csrf_exempt
# def stripe_webhook(request):
#     """Listen for webhooks from Stripe"""
#     # Setup
#     print('WEBHOOK!', 'working')
#     # You can find your endpoint's secret in your webhook settings
#     endpoint_secret = 'settings.STRIPE_WEBHOOK_SECRET'

#     # Get the webhook data and verify its signature
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, endpoint_secret
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)

#     # webhook_handler = StripeWebhookHandler(request)

#     # event_map = {
#     #     'payment_intent.succeeded': webhook_handler.handle_webhook_payment_intent_succeeded,
#     #     'payment_intent.payment_failed': webhook_handler.handle_webhook_payment_intent_failed,
#     # }

#     # event_type = event['type']    

#     # event_handler = event_map.get(event_type, webhook_handler.handle_webhook_event)
#     # response = event_handler(event)
#     # print(response)
#     # return response

#     # Handle the checkout.session.completed event
#     # if event_type == 'checkout.session.completed':
#     #     session = event['data']['object']
#     #     line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
#     #     print(line_items)
#     #     print(event_type)
    
#     # paymentId = payload['object']['id']
#     # amount = payload['object']['amount']
#     # paid = payload['object']['paid']

#     # print('PAY ID', paymentId)
#     # print('AMOUNT', amount)
#     # print('PAID', paid)

#     # StripePayment.objects.create(
#     #     paymentId=paymentId,
#     #     amount=amount,
#     #     paid=paid,
#     # )

#     return HttpResponse(status=200)


def get_plan_id(request, plan_id):
    plan_id = get_object_or_404(Plan, pk=plan_id)
    print(plan_id)
    context = {
        'plan_id': plan_id,
    }

    return render(request, 'subscriptions/edit_subscription_admin.html', context)


@login_required
def edit_subscription_admin(request, plan_id):
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
            messages.error(request, 'Failed to update plan. Please ensure the form is valid.')
    else:
        form = AddPlanForm(instance=plan)
        messages.info(request, f'You are editing {plan.plan_duration}')

    template = 'subscriptions/edit_subscription_admin.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)


def filter_user_has_order(user, order):
    has_order = []
    for name in order:
        if str(name.full_name) == str(user):
            has_order = name
    return has_order
