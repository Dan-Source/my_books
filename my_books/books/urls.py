from django.urls import path, include

urlpatterns = [
    path('api/', include('books.api.urls')),
]
