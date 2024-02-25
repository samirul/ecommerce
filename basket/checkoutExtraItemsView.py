from basket.basket import NavBar_Basket_count
from products.models import Cart
from basket.checkout import PriceCalculate, ShippingPriceCalculator


class CheckoutsExtraTemplateItemViews:
    def __init__(self, request):
        self.request = request
        self.checkouts = Cart.objects.filter(user=self.request.user)

        self.cart_product_items = [items for items in Cart.objects.all() if items.user == self.request.user]
        self.shipping_amount_calculator = ShippingPriceCalculator(request=self.request, cart_product_items=self.cart_product_items, shipping_amount=50)
        self.shipping_amount = self.shipping_amount_calculator.shipping_calculate()
        self.price_calculate = PriceCalculate(cart_product_items=self.cart_product_items, shipping_amount=self.shipping_amount)
        self.price, self.total_price = self.price_calculate.calculate()
        self.cart_count = NavBar_Basket_count(request=self.request)

        self.checkout_product_titles = []
        self.product_quantity_price = []

        self.total_discount_price = []
        self.discounted_price = []

    def cartExtraDataItems(self):

        for check in self.checkouts:
            check.price = self.total_price
            check.save()
            self.checkout_product_titles.append(check.product.product_title)
            self.product_quantity_price.append(check.product_quantity_price)


        return (self.shipping_amount, 
                self.price, self.total_price, 
                self.cart_count, self.checkout_product_titles,
                self.product_quantity_price)
    
    def CouponApply(self):
        for coupon in self.checkouts:
            if coupon.coupon:
                self.total_discount_price.append(self.total_price - coupon.coupon.discount_price)
                self.discounted_price.append(coupon.coupon.discount_price)
                coupon.price = self.total_price - coupon.coupon.discount_price
                coupon.save()

        return self.total_discount_price, self.discounted_price

        


