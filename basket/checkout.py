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
        


class GSTCalculator:
    def __init__(self, request, total_price):
        self.products = Cart.objects.filter(user=request.user)
        self.gst_zero_percent = ['Vegetables', 'Fruits', 'Cereals', 'Meat', 'Fish', 'Poultry']
        self.gst_five_percent = ['Tea', 'Coffee', 'Edible oil', 'Sugar', 'Spices']
        self.gst_twelve_percent = ['']
        self.gst_eighteen_percent = ['']
        self.total_price = total_price
        self.gst = 0
        self.gst_price = 0
        self.total_price_after_gst = 0
            
    def calculate(self):
        try:
            for product in self.products:
                if product.product.product_type.product_type_name in self.gst_zero_percent:
                    self.gst_price += self.total_price * (self.gst/100)
                    self.total_price_after_gst += self.gst_price + self.total_price
                
                elif product.product.product_type.product_type_name in self.gst_five_percent:
                    self.gst = 5
                    self.gst_price += self.total_price * (self.gst/100)
                    self.total_price_after_gst += self.gst_price + self.total_price
                
                elif product.product.product_type.product_type_name in self.gst_twelve_percent:
                    self.gst = 12
                    self.gst_price += self.total_price * (self.gst/100)
                    self.total_price_after_gst += self.gst_price + self.total_price
                
                elif product.product.product_type.product_type_name in self.gst_eighteen_percent:
                    self.gst = 18
                    self.gst_price += self.total_price * (self.gst/100)
                    self.total_price_after_gst += self.gst_price + self.total_price

            return self.gst_price, self.total_price_after_gst
        except Exception:
            self.total_price_after_gst = self.total_price
            return self.gst_price, self.total_price_after_gst
            
                         
