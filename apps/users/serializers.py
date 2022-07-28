from apps.users.models import User
from rest_framework import serializers


class UsersSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active')