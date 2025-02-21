"""
    EEMI E-commerce project, 2025
    E-commerce website in Django
    file description:
    This file is used to register the models in the admin interface
"""

from django.contrib import admin
from .models import product

admin.site.register(product)