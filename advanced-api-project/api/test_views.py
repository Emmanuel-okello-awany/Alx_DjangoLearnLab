from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book

class BookAPITestCase(TestCase):

    def setUp(self):
        """Set up a test user and log in."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Ensure session login

        self.book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2023)

    def test_create_book(self):
        """Ensure authenticated users can create a book."""
        data = {"title": "New Book", "author": "New Author", "publication_year": 2024}
        response = self.client.post("/books/", data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)  # Verify response data

    def test_get_books(self):
        """Ensure books can be retrieved."""
        response = self.client.get("/books/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure response contains books

    def test_update_book(self):
        """Ensure authenticated users can update a book."""
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2024}
        response = self.client.put(f"/books/{self.book.id}/", data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")  # Check updated data

    def test_delete_book(self):
        """Ensure authenticated users can delete a book."""
        response = self.client.delete(f"/books/{self.book.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)  # Ensure response has no content
