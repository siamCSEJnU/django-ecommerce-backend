from django.urls import path
from .views import cart_items, create_checkout_session

urlpatterns = [
    path("", cart_items),
    path("checkout/", create_checkout_session),
]
