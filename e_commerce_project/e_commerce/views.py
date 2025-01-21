from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import product

# Create your views here
def product_list(request):
    products = product.objects.all().order_by('-created_at').all()
    return render(request, 'e_commerce/product_list.html', {'products': products})
