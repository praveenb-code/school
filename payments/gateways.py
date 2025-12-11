import os, json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest

def create_stripe_payment_intent(amount, currency='inr', metadata=None):
    try:
        import stripe
    except Exception:
        raise RuntimeError('stripe library not installed')
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY','')
    intent = stripe.PaymentIntent.create(amount=int(float(amount)*100), currency=currency, metadata=metadata or {})
    return intent

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE','')
    secret = os.environ.get('STRIPE_WEBHOOK_SECRET','')
    try:
        import stripe
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY','')
        if secret:
            event = stripe.Webhook.construct_event(payload, sig_header, secret)
        else:
            event = json.loads(payload)
    except Exception:
        return HttpResponseBadRequest()
    # handle event types here
    return HttpResponse(status=200)

def create_razorpay_order(amount, currency='INR', receipt=None):
    try:
        import razorpay
    except Exception:
        raise RuntimeError('razorpay library not installed')
    client = razorpay.Client(auth=(os.environ.get('RAZORPAY_KEY_ID',''), os.environ.get('RAZORPAY_KEY_SECRET','')))
    order = client.order.create({'amount': int(float(amount)*100), 'currency': currency, 'receipt': receipt or 'rcpt'})
    return order

@csrf_exempt
def razorpay_webhook(request):
    # validate signature, etc.
    return HttpResponse(status=200)
