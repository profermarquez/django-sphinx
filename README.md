# Install entorno virtual
virtualenv -p "path/Python312/python.exe" env
cd .\env\
cd .\Scripts\
.\activate
# crear proyecto de django
pip install django
django-admin startproject tienda
cd tienda
python manage.py startapp productos
# crear migraciones y levantar el servidor
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# Instalar sphinx
pip install sphinx
#  Inicializar Sphinx en tu proyecto
sphinx-quickstart

# Comandos de generacion en Sphinx
make html
make clean

# for django
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']

import os
import sys
import django
sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings') # varia según el nombre del proyecto
django.setup()

# rst files example index
tienda documentation
====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   productos

# example model class
Productos
=========

.. automodule:: productos.models
   :members:
   :undoc-members:
   :show-inheritance:
