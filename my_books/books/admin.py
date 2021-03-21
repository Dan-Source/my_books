from django.contrib import admin
from my_books.books.models import Books, Category
from django.contrib.auth.models import Group

@admin.register(Books)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','author')
    list_filter = ('category',)

admin.site.register(Category)

admin.site.unregister(Group)

admin.site.site_header = "Books Admin"
