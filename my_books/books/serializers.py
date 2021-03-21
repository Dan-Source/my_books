from rest_framework import serializers
from my_books.books.models import Books, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class BooksSerializer(serializers.ModelSerializer):
    #category = CategorySerializer()

    class Meta:
        model = Books
        fields = ['pk','name', 'author', 'pages','user','category']
