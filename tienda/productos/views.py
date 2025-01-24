"""views de la app productos"""
from django.shortcuts import render
from .models import Producto

def home(request):
    """
    vista home de la tienda de productos, retorna todos los productos   
    """
    productos = Producto.objects.all()
    return render(request, 'productos/home.html', {'productos': productos})
