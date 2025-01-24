"""Modelo de la aplicación productos."""
from django.db import models

class Producto(models.Model):
    """
    Representa un producto en nuestra tienda.

    Args:
        nombre (str): Nombre del producto.
        descripcion (str): Descripción detallada del producto.
        precio (Decimal): Precio del producto.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Agrega más campos según tus necesidades (imagen, categoría, etc.)