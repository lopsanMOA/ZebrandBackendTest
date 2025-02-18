from rest_framework import serializers
from users.models import User


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', "is_admin"]
        extra_kwargs = {'password': {'write_only': True}}
