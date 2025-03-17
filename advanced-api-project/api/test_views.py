from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book

class BookAPITestCase(TestCase):

    def setUp(self):
        """Set up a test user and use session login."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Ensure login

        self.book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2023)

    def test_create_book(self):
        """Ensure authenticated users can create a book."""
        data = {"title": "New Book", "author": "New Author", "publication_year": 2024}
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        """Ensure books can be retrieved."""
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        """Ensure authenticated users can update a book."""
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2024}
        response = self.client.put(f"/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """Ensure authenticated users can delete a book."""
        response = self.client.delete(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
