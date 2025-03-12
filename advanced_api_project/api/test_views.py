from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        """
        Setup initial data for testing.
        """
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password')
        # Create test author
        self.author = Author.objects.create(name="J.K. Rowling")
        # Create test books
        self.book1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )
        # Create an API client
        self.client = APIClient()

    def test_create_book(self):
        """
        Ensure we can create a new book with valid data.
        """
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # One more book should be added

    def test_update_book(self):
        """
        Ensure we can update an existing book.
        """
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'Harry Potter and the Sorcerer\'s Stone - Updated',
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(f'/api/books/{self.book1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter and the Sorcerer\'s Stone - Updated')

    def test_delete_book(self):
        """
        Ensure we can delete an existing book.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # One book should be deleted

    def test_get_book_list(self):
        """
        Ensure we can retrieve a list of books.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We should have two books

    def test_get_book_detail(self):
        """
        Ensure we can retrieve details of a single book.
        """
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_filter_books(self):
        """
        Ensure we can filter books by title and author.
        """
        response = self.client.get('/api/books/?title=Harry Potter and the Sorcerer\'s Stone')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book should match

    def test_search_books(self):
        """
        Ensure we can search books by title or author name.
        """
        response = self.client.get('/api/books/?search=Harry')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books should match

    def test_order_books(self):
        """
        Ensure we can order books by title or publication year.
        """
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.book2.title)  # The second book should come first (latest year)

    def test_permissions(self):
        """
        Ensure permissions are correctly enforced.
        """
        # Test unauthenticated access to create a book
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test authenticated access to create a book
        self.client.login(username='testuser', password='password')
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
