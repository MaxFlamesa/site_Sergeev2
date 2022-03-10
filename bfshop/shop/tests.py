from django.test import TestCase

from shop.models import User, Product, Order

# Create your tests here.

class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(login = 'aboba', password = '123')
        Product.objects.create(name = 'aaa', price = 12)
        Product.objects.create(name = 'bbb', price = 142)

    def test_user_str(self):
        a = User.objects.get(id = 1)
        self.assertEqual(a.login, str(a)) 

    def test_product_str(self):
        a = Product.objects.all()
        for i in a:
            self.assertEqual(i.name, str(i))      