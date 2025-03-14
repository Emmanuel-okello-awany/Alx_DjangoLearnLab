from django.urls import path
from .views import example_form_view

urlpatterns = [
    path("example/", example_form_view, name="example_form"),
]
