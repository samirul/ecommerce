from products.models import Cart
from django.db.models import Sum

class PriceCalculate:
    def __init__(self, cart_product_items, shipping_amount):
        self.amount = 0
        self.shipping_amount = shipping_amount
        self.total_amount = 0
        self.cart_product_items = cart_product_items


    def calculate(self):
        if self.cart_product_items:
            for item in self.cart_product_items:
                product_quantity_price = (item.quantity * item.product.product_discounted_price)
                self.amount += product_quantity_price
            self.total_amount = self.amount + self.shipping_amount
        return self.amount, self.total_amount
        

class ShippingPriceCalculator:
    def __init__(self, request, cart_product_items, shipping_amount):
        self.request = request
        self.shipping_amount = shipping_amount
        self.none_amount = 0
        self.cart_product_items = cart_product_items

    def shipping_calculate(self):
        total_quantity = Cart.objects.filter(user=self.request.user).aggregate(Sum('quantity'))['quantity__sum']
        try:
            price_calculate = PriceCalculate(cart_product_items=self.cart_product_items, shipping_amount=self.shipping_amount)
            price, _ = price_calculate.calculate()
            if total_quantity >= 2 and total_quantity < 4:
                self.shipping_amount = 45
            if total_quantity >= 4 and total_quantity < 6:
                self.shipping_amount = 35
            if total_quantity >= 6 and total_quantity < 8:
                self.shipping_amount = 25
            if total_quantity >= 8 and price < 3000:
                self.shipping_amount = 15
            if price >= 3000:
                self.shipping_amount = 0
            return self.shipping_amount
        except Exception:
            return self.none_amount
        



                         
