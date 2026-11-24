from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active']

        read_only_fields = ['id', 'username']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'username']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)