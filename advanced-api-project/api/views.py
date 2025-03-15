from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.utils import timezone  
from rest_framework import generics, permissions, serializers  
 



class BookListView(generics.ListAPIView):
    """Retrieve all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookCreateView(generics.CreateAPIView):
    """Create a new book entry with validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Ensure publication_year is not in the future."""
        book = serializer.validated_data
        if book['publication_year'] > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """Update book entry with validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        """Validate the updated publication year."""
        book = serializer.validated_data
        if book['publication_year'] > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """Delete a book entry. Requires authentication."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

