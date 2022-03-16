from django.shortcuts import render, redirect   
from django.http import HttpResponse
from shop.models import Product, Order, User, List
from bfshop.settings import MEDIA_ROOT
from django.contrib.auth import authenticate, logout as lt, login as ln
from shop.forms import LoginForm

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    return render(request, 'shop/catalogue.html', {'all_products' : all_products})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            ln(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'shop/login_page.html', {'form' : form})

def logout(request):
    lt(request)
    print(request.user)
    return redirect('index')

    