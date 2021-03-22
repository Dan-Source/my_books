from django.contrib import admin
from my_books.books.models import Books, Category



@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk','name','author')
    list_filter = ('category',)

admin.site.register(Category)

admin.site.site_header = "Books Admin"
