from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
