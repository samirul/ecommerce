class PriceCalculate:
    def __init__(self, cart_product_items, shipping_amount):
        self.amount = 0.0
        self.shipping_amount = shipping_amount
        self.total_amount = 0.0
        self.cart_product_items = cart_product_items


    def calculate(self):
        if self.cart_product_items:
            for item in self.cart_product_items:
                product_quantity_price = (item.quantity * item.product.product_discounted_price)
                self.amount += product_quantity_price
            self.total_amount = self.amount + self.shipping_amount
        return self.amount, self.total_amount
        


                
