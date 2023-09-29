from django.urls import path
from .views import upload_algo, list_algos, delete_algo

urlpatterns = [
    path('upload/', upload_algo, name='upload_algo'),
    path('list/', list_algos, name='list_algos'),
    path('algorithms/delete/<int:algo_id>/', delete_algo, name='delete_algo')

]
