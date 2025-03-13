from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

