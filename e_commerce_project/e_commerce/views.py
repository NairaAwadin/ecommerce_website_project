from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import product

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

