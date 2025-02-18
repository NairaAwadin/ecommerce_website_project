from django.urls import path
from .import views
from .views import add_to_cart, display_cart, clear_cart
urlpatterns = [
    path('', views.product_list, name='product_list'),
    #path('product/<int:id>', views.product_details, name='product_details'),
    path('<int:id>/', views.product_details, name='product_details'),
    path('cart/', display_cart, name='display_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    #path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
]