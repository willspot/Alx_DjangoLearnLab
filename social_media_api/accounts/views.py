from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from .models import CustomUser

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                 password=serializer.validated_data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response({"error": "Invalid credentials"}, status=400)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = CustomUser.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({"message": "User followed successfully"})

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = CustomUser.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": "User unfollowed successfully"})