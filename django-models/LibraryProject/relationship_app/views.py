# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  
    context_object_name = "library" 
     
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library System!")  # Simple response for testing

