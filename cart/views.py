from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def cart_items(request):
    if request.method == "GET":
        items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return Response({"error": "Cart is empty"}, status=400)

    line_items = []
    for item in cart_items:
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(item.product.price * 100),
                    "product_data": {
                        "name": item.product.title,
                    },
                },
                "quantity": item.quantity,
            }
        )

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=settings.DOMAIN_URL + "success/",
        cancel_url=settings.DOMAIN_URL + "cancel/",
    )
    return Response({"checkout_url": session.url})
