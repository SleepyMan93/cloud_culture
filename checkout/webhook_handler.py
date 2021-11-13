from django.http import HttpResponse

class StripeWH_Handler:
    """ Handles Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown or unexpected webhook event 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type2"]}',
            status=200)