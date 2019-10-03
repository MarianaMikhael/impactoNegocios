from django.urls import path

from .views import index, create_sistema, update_sistema, delete_sistema

urlpatterns = [
    path('index/', index, name='index_sistemas'),
    path('create/', create_sistema, name='create_cadastro'),
    path('update/<int:cod_Sistema>/', update_sistema, name='update_cadastro'),
    path('delete/<int:cod_Sistema>/', delete_sistema, name='delete_cadastro'),
]
