from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Agrega más URLs para tus otras vistas
]