from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product, Order, User, List
from bfshop.settings import MEDIA_ROOT

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    return render(request, 'shop/catalogue.html', {'all_products' : all_products})

def login_page(request):
    return render(request, 'shop/login_page.html', {})