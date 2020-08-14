from django.contrib import admin
from django.urls import path, include
from core.views import home,StripeView,SuccessView,SubscribeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stripe-checkout/', StripeView.as_view(), name='stripeu'),
    path('accounts/', include('allauth.urls')),
    path('stripe/', include("djstripe.urls", namespace="djstripe")),
    path('thankyou/', SuccessView.as_view(),name='thankyou'),
    path('subscribe/', SubscribeView.as_view(),name='subscribe'),


]
