"""
    EEMI E-commerce project, 2025
    E-commerce website in Django
    file description:
    This file is used to link the views to the urls
"""

from django.urls import path
from .import views
from .views import add_to_cart, display_cart, clear_cart, increase_quantity, decrease_quantity, register_order, order_history

urlpatterns = [
    path('', views.product_list, name='product_list'),
    #path('product/<int:id>', views.product_details, name='product_details'),
    path('<int:id>/', views.product_details, name='product_details'),
    path('cart/', display_cart, name='display_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    #path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('cart/increase/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('order/', register_order, name='register_order'),
    path('order/history/', order_history, name='order_history'),
]