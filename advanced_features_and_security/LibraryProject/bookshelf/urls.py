from django.urls import path
from .views import example_form_view, book_list_view

urlpatterns = [
    path("example/", example_form_view, name="example_form"),
    path("book_list/", book_list_view, name="book_list"),
]
