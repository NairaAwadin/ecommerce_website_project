from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import product
from .cart import panier

# Create your views here
def product_list(request):
    query = request.GET.get('q', '')
    products = product.objects.all().order_by('-created_at').all()
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    if query:
        products = products.filter(name__icontains=query)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'e_commerce/product_list.html', {'products': products})

def product_details(request, id):
    details = product.objects.get(id=id)
    return render(request, 'e_commerce/product_details.html', {'details': details})

def afficher_panier(request):
    #panier = request.session.get('panier', {})

    #for item in panier.values():
      #  print(f"Produit: {item}, Price: {item.get('price')}") 

    #total = sum(float(item['price'] or 0) * item['quantite'] for item in panier.values())

    #return render(request, 'cart.html', {'panier': panier, 'total': total})
    return render(request,'cart.html')

def ajouter_au_panier(request, produit_id):
    panier = panier(request)
    panier.ajouter(produit_id)
    print(f"Produit récupéré: {product.name}, Prix: {product.price}")
    return redirect('afficher_panier')

def supprimer_du_panier(request, produit_id):
    panier = panier(request)
    panier.supprimer(produit_id)
    return redirect('afficher_panier')

def vider_panier(request):
    panier = panier(request)
    panier.vider()
    return redirect('afficher_panier')
