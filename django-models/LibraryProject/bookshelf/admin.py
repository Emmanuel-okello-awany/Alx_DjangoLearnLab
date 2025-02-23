from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in the admin list view
    list_filter = ('publication_year', 'author')  # Filter options in the admin panel
    search_fields = ('title', 'author')  # Search functionality for book title and author

