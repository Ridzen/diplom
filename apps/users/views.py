from rest_framework import generics
from .serializers import UsersSerializers
from rest_framework.permissions import IsAdminUser
from apps.users.models import User

# Users


class UsersView(generics.ListAPIView):
    serializer_class = UsersSerializers
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
