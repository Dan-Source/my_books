from django.contrib import admin
from my_books.books.models import Books, Category

admin.site.register(Books)
admin.site.register(Category)
