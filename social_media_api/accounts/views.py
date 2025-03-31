from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

User = get_user_model()  # Ensure we are using the custom user model

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user': UserSerializer(user).data})
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """Allows an authenticated user to follow another user."""
    target_user = get_object_or_404(User, id=user_id)  # Use get_user_model() instead of CustomUser
    request.user.following.add(target_user)  # Use the following ManyToMany field
    return Response({"message": f"You are now following {target_user.username}"}, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """Allows an authenticated user to unfollow another user."""
    target_user = get_object_or_404(User, id=user_id)  # Use get_user_model() instead of CustomUser
    request.user.following.remove(target_user)  # Use the following ManyToMany field
    return Response({"message": f"You have unfollowed {target_user.username}"}, status=200)
