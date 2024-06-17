from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Check if the username already exists (case insensitive)
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError('Username is taken')

        return data

    def create(self, validated_data):
        username = validated_data['username'].lower()
        password = validated_data['password']

        # Create the user with a lowercased username
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        return {
            'username': user.username,
            'message': 'User created successfully'
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError('Username and password are required')

        # Case insensitive user lookup and authentication
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        refresh = RefreshToken.for_user(user)

        return {
            'username': user.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }