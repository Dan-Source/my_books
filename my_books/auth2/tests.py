from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from my_books.books.models import User

from my_books.auth2.serializers import (
    RegisterSerializer, 
    MyTokenObtainPairSerializer
)

from my_books.auth2.views import MyObtainTokenPairView, RegisterView

factory = APIRequestFactory()


class RegisterViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste')
        self.user.set_password('#pass123')
        self.user.is_superuser = True
        self.user.save()

    def test_create_ok(self):
        data = {
            'username': 'teste_02', 
            'password': '#pass123',
            'password2': '#pass123',
            'email': 'teste@mail.com',
            'first_name':'Teste name',
            'last_name': 'Teste name',
        }
        request = factory.post('/auth/register/', data)
        view = RegisterView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
