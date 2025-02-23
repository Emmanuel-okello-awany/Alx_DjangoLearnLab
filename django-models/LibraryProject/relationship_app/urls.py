from django.urls import path
from .views import list_books, LibraryDetailView, home ,login_view, logout_view,register_view # Ensure `list_books` is imported


urlpatterns = [
    path("", home, name="home"),  # Add this line for the default homepage
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
