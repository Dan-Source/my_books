from django.urls import path
from my_books.auth2.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'auth2'

urlpatterns = [
    path(
        'login/', MyObtainTokenPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path('login/refresh/', TokenRefreshView.as_view(), 
    name='token_refresh'
    ),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
