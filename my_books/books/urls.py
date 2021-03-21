from django.urls import path, include
from .views import BooksListApiView, BooksDetailApiView  # BooksListViewSet,
from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'',BooksListViewSet, basename='books')

app_name = 'books'
urlpatterns = [
   path('', BooksListApiView.as_view()),
   path('detail/<int:book_id>/', BooksDetailApiView.as_view()),
   # path('list/', include(router.urls))
]
