from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user, login_user, verify_email, user_profile

urlpatterns = [
    path("register/", register_user),
    path("login/", login_user),
    path("verify-email/<uidb64>/<token>/", verify_email),
    path("profile/", user_profile),
    path(
        "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
