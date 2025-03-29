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

# Follow User View
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def post(self, request, user_id):
        # Try to find the user to follow
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the current user (who is trying to follow someone)
        current_user = request.user

        if current_user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the current user's following list (ManyToManyField)
        current_user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

# Unfollow User View
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def post(self, request, user_id):
        # Try to find the user to unfollow
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the current user (who is trying to unfollow someone)
        current_user = request.user

        if current_user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the user from the current user's following list (ManyToManyField)
        current_user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

# View to get a list of users the current user is following
class FollowingListView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def get(self, request):
        # Get the current authenticated user
        current_user = request.user
        
        # Get all users that the current user is following
        following = current_user.following.all()

        # Prepare the response data (list of followed users)
        following_data = [{"id": user.id, "username": user.username} for user in following]
        
        return Response(following_data, status=status.HTTP_200_OK)