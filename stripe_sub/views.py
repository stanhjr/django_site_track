import stripe

from djstripe.models import Customer

from rest_framework.response import Response
from rest_framework.views import APIView

from django_site_track.settings import STRIPE_TEST_SECRET_KEY, STRIPE_PLAN

PLAN = {
    "sub-1-truck": "some_id_product",
    "sub-12-month": STRIPE_PLAN,
    "sub-36-month": "some_id_product",
}


class GetSessionIdAPIView(APIView):
    def get(self, request):
        customer, _ = Customer.get_or_create(subscriber=request.user)
        plan = PLAN.get(request.GET.get("plan"))
        if not plan:
            return Response(status=404)

        stripe.api_key = STRIPE_TEST_SECRET_KEY
        try:
            session = stripe.checkout.Session.create(
                customer=customer.id,
                payment_method_types=['card'],
                subscription_data={
                    'items': [{
                        'plan': plan,
                    }],
                },
                success_url='https://buymyfleet.net/',
                cancel_url='https://buymyfleet.net/',
            )

            data = {
                "session_id": session.id
            }
        except stripe.error.InvalidRequestError:
            return Response(status=404)

        return Response(data, status=200)
