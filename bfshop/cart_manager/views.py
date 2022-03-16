from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from shop.models import Product, Order, List, User
from django.views.decorators.http import require_POST
from shop.views import index


# Create your views here.

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.add(product = product, county = 1, update_county = False)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_manager/detail.html', {'cart' : cart})

def cart_release(request):
    cart = Cart(request)
    a = User.objects.all()
    order = Order(user_id = request.user, status = 'pending')
    order.save()
    for item in cart:
        list = List(order_id = order, product_id = item['product'], county = item['county'], pay_price = item['price'])
        list.save()
    cart.clear()
    return redirect('index')