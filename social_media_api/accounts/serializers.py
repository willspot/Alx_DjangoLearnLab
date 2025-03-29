from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user
        user = get_user_model().objects.create_user(**validated_data)

        # Create a token for the user
        token = Token.objects.create(user=user)

        # Return the user and token
        return user, token

# Serializer for user login (authentication)
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return user
        raise serializers.ValidationError("Invalid credentials")

# Serializer for token retrieval after login
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
