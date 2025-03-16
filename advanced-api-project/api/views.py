from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book

class BookAPITestCase(APITestCase):
    """Test case for CRUD operations on the Book API."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.book = Book.objects.create(title="Test Book", author="Author One", publication_year=2023)
        self.client.force_authenticate(user=self.user)  # Authenticate the client

    def test_create_book(self):
        """Ensure we can create a new book."""
        url = reverse("book-create")  # Ensure your urls.py has the correct name for this view
        data = {"title": "New Book", "author": "Author Two", "publication_year": 2024}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        """Ensure we can retrieve the list of books."""
        url = reverse("book-list")  # Ensure your urls.py has the correct name for this view
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return one book in the list

    def test_get_book_detail(self):
        """Ensure we can retrieve a single book."""
        url = reverse("book-detail", kwargs={"pk": self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        """Ensure we can update a book's details."""
        url = reverse("book-update", kwargs={"pk": self.book.id})
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2022}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Ensure we can delete a book."""
        url = reverse("book-delete", kwargs={"pk": self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_unauthenticated_user_cannot_create_book(self):
        """Ensure unauthenticated users cannot create a book."""
        self.client.logout()  # Remove authentication
        url = reverse("book-create")
        data = {"title": "Unauthorized Book", "author": "Unknown", "publication_year": 2023}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
