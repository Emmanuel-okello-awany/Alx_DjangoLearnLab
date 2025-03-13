from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing route for list-only view
    path('books/', BookList.as_view(), name='book-list'),

    # Register the ViewSet routes
    path('', include(router.urls)),  # This includes all routes for the BookViewSet
]

