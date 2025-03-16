from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    """Test case for Book API endpoints."""

    def setUp(self):
        """Set up test data and client authentication."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        self.book1 = Book.objects.create(title='Book One', author='Author One', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author Two', publication_year=2019)
        
        self.valid_data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2023
        }
        
        self.invalid_data = {
            'title': '',
            'author': 'New Author',
            'publication_year': 2030  # Future year (invalid case)
        }
    
    def test_get_books_list(self):
        """Ensure we can retrieve a list of books."""
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_book_detail(self):
        """Ensure we can retrieve details of a single book."""
        response = self.client.get(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
    
    def test_create_book(self):
        """Ensure an authenticated user can create a book."""
        response = self.client.post('/books/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_book_invalid_data(self):
        """Ensure validation errors are returned for invalid data."""
        response = self.client.post('/books/', self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update_book(self):
        """Ensure an authenticated user can update a book."""
        updated_data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(f'/books/{self.book1.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')
    
    def test_delete_book(self):
        """Ensure an authenticated user can delete a book."""
        response = self.client.delete(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_unauthenticated_access(self):
        """Ensure unauthenticated users cannot create, update, or delete books."""
        self.client.logout()
        response = self.client.post('/books/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)