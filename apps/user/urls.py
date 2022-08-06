from django.urls import path

from .views import (
    RegisterView, ActivationView,
    UserProfileUpdateView, ChangePasswordView,
    ForgotPasswordView, ForgotPasswordConfirmView, LogoutView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    # user sign up and password conf
    path('log-in/', TokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('forgot-password/confirm/', ForgotPasswordConfirmView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),

    path('activate/<str:email>/<str:activation_code>/',
         ActivationView.as_view(), name='activate'),

    # user profile
    path('user-profile/<int:pk>/',
         UserProfileUpdateView.as_view(), name='user-profile'),
    path('change-password/',
         ChangePasswordView.as_view(), name='change-password'),
    path('log-out/', LogoutView.as_view(), name="log-out")
]
