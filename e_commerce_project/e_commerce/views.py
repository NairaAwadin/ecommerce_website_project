from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import product

# Create your views here
def product_list(request):
    products = product.objects.all().order_by('-created_at').all()
    return render(request, 'e_commerce/product_list.html', {'products': products})

def product_details(request, id):
    details = product.objects.get(id=id)
    return render(request, 'e_commerce/product_details.html', {'details': details})
