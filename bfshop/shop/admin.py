from django.contrib import admin
from .models import Product, Order, User, List

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(List)