from django.urls import path
from . import views, gateways

urlpatterns = [
    path('', views.payment_list, name='payments_home'),
    path('create/', views.create_payment, name='create_payment'),
    path('receipt/<int:pk>/', views.payment_receipt, name='payment_receipt'),
    path('dashboard-data/', views.dashboard_data, name='dashboard_data'),
    path('stripe/webhook/', gateways.stripe_webhook, name='stripe_webhook'),
    path('razorpay/webhook/', gateways.razorpay_webhook, name='razorpay_webhook'),
]
