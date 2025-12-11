Payments App — Full Features Added
----------------------------------
What was added:
- payments app with models, forms, views, templates
- Stripe & Razorpay scaffolding (payments/gateways.py)
- DRF viewset (payments/api.py)
- Channels consumer (payments/consumers.py) and routing
- PDF receipt rendering helper (payments/utils.py)
- Templates for listing, receipt and simple dashboard polling via AJAX

Quick steps to enable:
1. Add 'payments', 'rest_framework', 'channels' to INSTALLED_APPS in settings.py
2. Configure ASGI_APPLICATION in settings.py and CHANNEL_LAYERS for Redis
3. Install dependencies: stripe, razorpay, weasyprint, djangorestframework, channels, channels-redis
4. Run migrations: python manage.py makemigrations payments && python manage.py migrate
5. Wire payments.urls into your project urls.py: path('payments/', include('payments.urls'))

Notes:
- Webhooks: configure webhook endpoints to point to /payments/stripe/webhook/ and /payments/razorpay/webhook/
- The code contains scaffolding and safety checks; please add secret keys via environment variables.
