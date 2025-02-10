from django.urls import path
from .import views
from .views import product_list, afficher_panier, ajouter_au_panier, supprimer_du_panier, vider_panier

urlpatterns = [
    path('', views.product_list, name='product_list'),
    #path('product/<int:id>', views.product_details, name='product_details'),
    path('<int:id>/', views.product_details, name='product_details'),
     path('panier/', afficher_panier, name='afficher_panier'),
    path('panier/ajouter/<int:produit_id>/', ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/supprimer/<int:produit_id>/', supprimer_du_panier, name='supprimer_du_panier'),
    path('panier/vider/', vider_panier, name='vider_panier'),
]