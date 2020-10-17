import json
import time
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from products.models import Product
from user_profile.models import UserProfile
from .models import ProductOrder, ProductLineOrder


class StripeWebhookHandler:
    """Handle Stripe webhooks to prevent the payment
    to go through but no order in the database"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email for their placed order"""
        customer_email = order.email
        email_subject = render_to_string(
            'checkout/confirmation_emails/send_confirmation_email_subject.txt',
            {'order': order})
        email_body = render_to_string(
            'checkout/confirmation_emails/send_confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_webhook_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_webhook_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pay_intent_id = intent.id
        shop_bag = intent.metadata.shop_bag
        save_user_info = intent.metadata.save_user_info
        subscription = intent.metadata.subscription

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        shop_total = round(intent.charges.data[0].amount / 100, 2)

        if subscription:
            profile = None
            username = intent.metadata.username

        if shop_bag:
            # Clean data in the shipping details
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None

            # Update profile information if save_user_info was checked
            profile = None
            username = intent.metadata.username
            if username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                if save_user_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.\
                        postal_code
                    profile.default_town_or_city = shipping_details.address.\
                        city
                    profile.default_street_address1 = shipping_details.\
                        address.line1
                    profile.default_street_address2 = shipping_details.\
                        address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()

            order_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    order = ProductOrder.objects.get(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        county__iexact=shipping_details.address.state,
                        shop_total=shop_total,
                        original_shop_bag=shop_bag,
                        stripe_pid=pay_intent_id,
                    )
                    product_order_exists = True
                    break
                except ProductOrder.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
            if product_order_exists:
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} |\
                        SUCCESS: Verified order already in database',
                    status=200)
            else:
                order = None
                try:
                    order = ProductOrder.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_shop_bag=shop_bag,
                        stripe_pid=pay_intent_id
                    )
                    for product_id, item_data in json.loads(shop_bag).items():
                        product = Product.objects.get(id=product_id)
                        if isinstance(item_data, int):
                            product_line_order = ProductLineOrder(
                                order=order,
                                product=product,
                                product_quantity=item_data,
                            )
                            product_line_order.save()
                        else:
                            for size, product_quantity\
                              in item_data['items_by_size'].items():
                                product_line_order = ProductLineOrder(
                                    order=order,
                                    product=product,
                                    product_quantity=product_quantity,
                                    product_size=size,
                                )
                                product_line_order.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} |\
                            ERROR: {e}',
                        status=500)
            self._send_confirmation_email(order)

        else:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} |\
                    SUCCESS: Created order in webhook',
                status=200)

    def handle_webhook_payment_intent_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
