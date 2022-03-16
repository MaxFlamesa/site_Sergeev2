from django.contrib import admin
from .models import Product, Order, User, List
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User, UserAdmin)
admin.site.register(List)