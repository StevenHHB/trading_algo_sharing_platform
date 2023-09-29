from .views import register, user_login, home
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('login', user_login, name='login'),
    path('', home, name='home')
]
