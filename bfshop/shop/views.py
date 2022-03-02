from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product, Order, User, List

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    print(Order.objects.all().filter(id = '1'))
    return render(request, 'shop/catalogue.html', {'all_products' : all_products})