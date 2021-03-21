from rest_framework import serializers
from my_books.books.models import Books

class BooksSerializer(serializers.Serializer):
    class Meta:
        model = Books
        fields = ['name', 'author', 'pages', 'user']
