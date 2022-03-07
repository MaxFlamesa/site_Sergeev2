from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm

# Create your views here.

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.add(product = product, county = 1, update_county = False)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_manager/detail.html', {'cart' : cart})