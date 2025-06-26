from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import User
from .serializers import (
    UserRegistrationSerializer,
    LoginSerializer,
    UserProfileSerializer,
)


# Create your views here.
@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        send_verification_email(user)
        return Response(
            {
                "message": "User registered. Please check your email to verify your account."
            },
            status=201,
        )
    return Response(serializer.errors, status=400)


def send_verification_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    verify_url = f"http://localhost:8000/users/verify-email/{uid}/{token}/"
    send_mail(
        subject="Verify your account",
        message=f"Click the link to verify your email:\n{verify_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )


@api_view(["GET"])
def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid)

    except Exception:
        return Response({"error": "Invalid verification link"}, status=400)

    if default_token_generator.check_token(user, token):
        user.is_verified = True
        user.save()
        return Response({"message": "Email verified successfully!"})
    return Response({"error": "Invalid or expired token"}, status=400)


@api_view(["POST"])
def login_user(request):
    serializer = LoginSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    return Response(serializer.errors, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data)
