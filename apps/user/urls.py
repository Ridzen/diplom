from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    # user sign up and password conf
    path('log-in/', TokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('forgot-password/confirm/', views.ForgotPasswordConfirmView.as_view(), name='forgot-password-confirm'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    # Email activation
    path('activate/<str:email>/<str:activation_code>/',
         views.ActivationView.as_view(), name='activate'),

    # user profile
    path('user-profile/<int:pk>/',
         views.UserProfileUpdateView.as_view(), name='user-profile'),
    path('change-password/',
         views.ChangePasswordView.as_view(), name='change-password'),
    path('log-out/', views.LogoutView.as_view(), name="log-out")
]
