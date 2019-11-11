from django.urls import path
from .views import home

urlpatterns = [
    path('homepage/', home, name='home')
]
