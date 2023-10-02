from products.models import Cart

class NavBar_Basket_count:
    def __init__(self, request):
        self.request = request
        self.cart = Cart

    def calculate(self):
        user = self.request.user
        if user.is_authenticated:
            return len(Cart.objects.filter(user=user))
            