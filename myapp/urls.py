from django.contrib import admin
from django.urls import path,include
from myapp.views import *
from . import views

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('webhook/', views.stripe_webhook),
]