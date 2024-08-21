from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ItemView, StripeSessionView, success_view, cancel_view

urlpatterns = [
    path("item/<int:id>", ItemView.as_view(), name='item'),
    path("buy/<int:id>", StripeSessionView.as_view(), name='buy-item'),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
] + static(settings.STATIC_URL)
