from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to = 'img/' , default = '')

    def __str__(self):
        return str(self.name)

class User(models.Model):
    login = models.TextField()
    password = models.TextField()

    def __str__(self):
        return str(self.login)

class Order(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    status = models.TextField()

    def __str__(self):
        return str(self.user_id.login) + '/' + str(self.status)

class List(models.Model):
    order_id = models.ForeignKey('Order', on_delete = models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete = models.CASCADE)
    county = models.IntegerField()
    pay_price = models.FloatField()

    def __str__(self):
        return str(self.order_id.user_id) + ' -> ' + str(self.product_id.name) + ' x ' + str(self.county)

    