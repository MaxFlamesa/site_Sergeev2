from shop.models import Product
from django.conf import settings

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['total_price'] = item['price'] * item['county']
            yield item
    
    def __str__(self):
        ans = ''
        for i in self.cart:
            ans += str(self.cart[i])
        return ans

    def add(self, product, county, update_county = False):
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id] = {'county': 0,
                                    'price': product.price}
        if update_county:
            self.cart[product_id]['county'] = county
        else:
            self.cart[product_id]['county'] += county
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True