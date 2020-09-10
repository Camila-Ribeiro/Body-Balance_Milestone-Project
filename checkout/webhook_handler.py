from django.http import HttpResponse


class StripeWebhookHandler:
    """Handle Stripe webhooks to prevent the payment 
    to go through but no order in the database"""

    def __init__(self, request):
        self.request = request

    def handle_webhook_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)