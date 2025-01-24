"""Configuración de la aplicación productos."""
from django.apps import AppConfig


class ProductosConfig(AppConfig):
    """
    Representa clase ProductosConfig

    Atributos:
        name (str): Nombre de la aplicación.
        default_auto_field (str): Campo autoincremental.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'
