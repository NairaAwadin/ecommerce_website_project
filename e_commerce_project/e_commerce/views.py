from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import product
from .cart import cart

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

cart = cart()

def display_cart(request):
    total_price = cart.total_price()
    return render(request, 'e_commerce/cart.html', {'cart': cart.items, 'total': cart.total_price()})

def add_to_cart(request, product_id):
    cart.add(product_id)
    return redirect('display_cart')

"""def remove_from_cart(request, product_id: int):
    cart.remove(product_id)
    return redirect('display_cart')"""

def clear_cart(request):
    cart.clear()
    return redirect('display_cart')

def increase_quantity(request, product_id):
    cart.increase_quantity(product_id)
    return redirect('display_cart')

def decrease_quantity(request, product_id):
    cart.decrease_quantity(product_id)
    return redirect('display_cart')