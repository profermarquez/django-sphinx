# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test2'
copyright = '2025, sebas'
author = 'sebas'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']


templates_path = ['_templates']
exclude_patterns = [
    'env/**',  # Excluir archivos de tu entorno virtual
    'env/Lib/site-packages/**',  # Excluir paquetes instalados
    '**/LICENSE.rst',  # Excluir todos los archivos LICENSE.rst
    '**/templates/**',  # Excluir plantillas
]

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
import django
sys.path.insert(0, os.path.abspath('../'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings') # varia según el nombre del proyecto
django.setup()