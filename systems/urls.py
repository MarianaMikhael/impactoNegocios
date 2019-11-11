from django.urls import path

from .views import ac, acn, acn_plus
from .views import create_sistema, update_sistema, delete_sistema

urlpatterns = [
    path('index/ac/', ac, name='index_ac'),
    path('index/acn/', acn, name='index_acn'),
    path('index/acn_plus/', acn_plus, name='index_acn_plus'),
    path('create/', create_sistema, name='create_cadastro'),
    path('update/<int:cod_Sistema>/', update_sistema, name='update_cadastro'),
    path('delete/<int:cod_Sistema>/', delete_sistema, name='delete_cadastro'),
]
