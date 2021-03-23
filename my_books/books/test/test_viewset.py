import json

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate


from my_books.books.models import Books, Category, User
from my_books.books.serializers import BooksSerializer, CategorySerializer

from my_books.books.views import (
    BooksDetailApiView,
    BooksListApiView,
    CategoryViewSet,
)


factory = APIRequestFactory()


class CategoryViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste')
        self.user.set_password('#pass123')
        self.user.is_superuser = True
        self.user.save()

        self.category = Category.objects.create(name='Teste')
        self.category.save()

    def test_create(self):
        data = {'name': 'teste 02'}
        request = factory.post('/books/category/', data)
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        view = CategoryViewSet.as_view({'get': 'list'})
        request = factory.get('/books/category/')
        force_authenticate(request, user=self.user)
        response = view(request)
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste')
        self.user.set_password('#pass123')
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()

        self.category = Category.objects.create(name='Teste Category')
        self.category.save()

        self.books = Books.objects.create(
            name='Books Teste',
            author='Author',
            user=self.user,
            pages=777,
            category=self.category
        )
        self.books.save()
    
    def test_create(self):
        data = {
            'name': 'Teste',
            'author': 'Author',
            'pages': 777,
            'user': self.user.id,
            'category': self.category.id,
        }

        request = factory.post('/books/', data)
        force_authenticate(request, user=self.user)
        view = BooksListApiView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all(self):
        view = BooksListApiView.as_view()
        request = factory.get('/books/')
        force_authenticate(request, user=self.user)
        response = view(request)
        books = Books.objects.filter(pk=self.user.id)
        serializer = BooksSerializer(books,many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product(self):
        view = BooksDetailApiView.as_view()
        request = factory.get('/books/',)
        force_authenticate(request, user=self.user)
        response = view(request, book_id=self.books.id)
        book = Books.objects.get(id=self.books.id)
        serializer = BooksSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete(self):
        view = BooksDetailApiView.as_view()
        endpoint = '/books/'
        request = factory.delete(endpoint)
        force_authenticate(request, user=self.user)
        response = view(request, book_id=self.books.id)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
