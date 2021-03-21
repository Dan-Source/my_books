from django.urls import path
from .views import BooksListApiView
from rest_framework import routers

app_name = 'books'

urlpatterns = [
   path('', BooksListApiView.as_view()),
]
