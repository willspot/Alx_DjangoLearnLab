from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user, token = serializer.save()
        return Response({
            'user': UserRegistrationSerializer(user).data,
            'token': token.key
        })

# User Login View
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)  # Get or create token
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Profile View
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer  # Reuse UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Return the current authenticated user


CustomUser = get_user_model()

# Follow user view
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Get the user to follow
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the current authenticated user
        current_user = request.user

        if current_user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the current user's following list
        current_user.following.add(user_to_follow)
        return Response({"detail": f"Now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

# Unfollow user view
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Get the user to unfollow
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the current authenticated user
        current_user = request.user

        if current_user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the user from the current user's following list
        current_user.following.remove(user_to_unfollow)
        return Response({"detail": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)


class FollowingListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        following = current_user.following.all()  # Get all the users the current user is following
        following_data = [{"username": user.username} for user in following]
        return Response(following_data, status=status.HTTP_200_OK)