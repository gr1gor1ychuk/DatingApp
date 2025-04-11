from product import Product
from user import User


class Order:
    def __init__(self, order_id: int, user: User):
        self.id = order_id
        self.user = user
        self.products = []
        self.user.add_order(self)

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)
