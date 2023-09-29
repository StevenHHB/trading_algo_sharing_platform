from .views import register, user_login, home, user_logout
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout')
]
