from shop.models import Product

class  Cart(object):
    def __init__(self):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

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