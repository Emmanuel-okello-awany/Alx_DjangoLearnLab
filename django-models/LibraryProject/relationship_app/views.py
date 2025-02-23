# Create your views here.
from django.shortcuts import render
from .models import Book



def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

from .models import Library
from django.views.generic.detail import DetailView 

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  
    context_object_name = "library" 
     
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library System!")  # Simple response for testing

