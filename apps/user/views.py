from requests import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (RegisterSerializer, UserProfileSerializer, ChangePasswordSerializer,
                          ForgotPasswordSerializer, ForgotPassCompleteSerializer, UpdateProfileSerializer)

# Create your views here.


class RegisterView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            obj = serializer.save()
            obj.set_password(obj.activation_code)


class ActivationView(APIView):

    def get(self, request, email, activation_code):
        user = User.objects.filter(
            email=email,
            activation_code=activation_code
        ).first()
        msg_ = (
            "User does not exist",
            "Activated!"
        )
        if not user:
            return Response(msg_, 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response(msg_[-1], 200)


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response(
                "Reset code was sent to your email!", 200
            )


class ForgotPasswordConfirmView(APIView):
    def post(self, request):
        serializer = ForgotPassCompleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                "Your password was successfully updated!", 200
            )


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
