from django.urls import path, include
from my_books.books.views import (
    CategoryViewSet,
    BooksListApiView, 
    BooksDetailApiView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='books')

app_name = 'books'
urlpatterns = [
   path('', BooksListApiView.as_view()),
   path('detail/<int:book_id>/', BooksDetailApiView.as_view()),
   path('', include(router.urls))
]
