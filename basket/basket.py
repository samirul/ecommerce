from products.models import Cart

class NavBar_Basket_count:
    def __init__(self, request):
        self.request = request
        self.cart = Cart
        self.qty = 0

    def calculate(self):
        user = self.request.user
        if user.is_authenticated:
            cart = Cart.objects.filter(user=user)
            for qty in cart:
                self.qty += qty.quantity
            return self.qty
            