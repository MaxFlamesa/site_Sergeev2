from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    price = models.FloatField()

class User(models.Model):
    login = models.TextField()
    password = models.TextField()

class Order(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    status = models.TextField()

class List(models.Model):
    order_id = models.ForeignKey('Order', on_delete = models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete = models.CASCADE)
    county = models.IntegerField()
    pay_price = models.FloatField()

    