from abc import ABC

from rest_framework import serializers
from .models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=4, required=False, write_only=True,
    )
    promo_code = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)

    class Meta:

        model = User
        fields = (
            'full_name', 'phone', 'email', 'password'
        )

    def validate(self, attrs):
        code = get_random_string(
            length=10,
            allowed_chars='1234567890#$%!?_'
        )
        attrs['password'] = code
        attrs['activation_code'] = code


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не найден!')

        return email

    def send_verification_email(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        send_mail(
            'Забыли пароль',
            f'Ваш код для изменения пароля - {user.activation_code}',
            'admin@gmail.com',
            [user.email]
        )


class ForgotPassCompleteSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=4, required=True)
    password_confirmation = serializers.CharField(min_length=4, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password1 = attrs.get('password')
        password2 = attrs.get('password_confirmation')
        code = attrs.get('code')
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError("Invalid confirmation code or email!")
        if password1 != password2:
            raise serializers.ValidationError("Passwords didn't match!")
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UpdateProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone', 'avatar')




