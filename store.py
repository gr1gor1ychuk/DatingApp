import unittest


class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def register(self):
        print(f"User {self.name} registered successfully.")

    def login(self):
        print(f"User {self.name} logged in.")

    def view_orders(self):
        return self.orders


class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price

    def get_info(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"


class Order:
    def __init__(self, order_id: int, user: User):
        self.id = order_id
        self.user = user
        self.products = []
        user.orders.append(self)

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)


class TestECommerceSystem(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Alice", "alice@example.com")
        self.product1 = Product(101, "Bike", 299.99)
        self.product2 = Product(102, "Helmet", 49.99)
        self.order = Order(1, self.user)

    def test_user_registration(self):
        self.assertEqual(self.user.name, "Alice")
        self.assertEqual(self.user.email, "alice@example.com")

    def test_user_orders_initially_empty(self):
        self.assertEqual(len(self.user.orders), 1)  # Order was added

    def test_add_product_to_order(self):
        self.order.add_product(self.product1)
        self.assertIn(self.product1, self.order.products)

    def test_remove_product_from_order(self):
        self.order.add_product(self.product1)
        self.order.remove_product(self.product1)
        self.assertNotIn(self.product1, self.order.products)

    def test_calculate_total(self):
        self.order.add_product(self.product1)
        self.order.add_product(self.product2)
        self.assertEqual(self.order.calculate_total(), 349.98)

    def test_product_info(self):
        self.assertEqual(self.product1.get_info(), "Product: Bike, Price: $299.99")

    def test_multiple_orders_for_user(self):
        order2 = Order(2, self.user)
        self.assertEqual(len(self.user.orders), 2)

    def test_order_associated_with_user(self):
        self.assertIn(self.order, self.user.view_orders())

    def test_remove_nonexistent_product(self):
        self.order.remove_product(self.product1)  # Should not cause an error
        self.assertEqual(len(self.order.products), 0)

    def test_empty_order_total(self):
        self.assertEqual(self.order.calculate_total(), 0.0)


if __name__ == "__main__":
    unittest.main()
