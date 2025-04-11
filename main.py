from user import User
from product import Product
from order import Order


def main():
    user1 = User(1, "Alice", "alice@example.com")
    user1.register()
    user1.login()

    product1 = Product(101, "Bike", 299.99)
    product2 = Product(102, "Helmet", 49.99)

    order1 = Order(1, user1)
    order1.add_product(product1)
    order1.add_product(product2)

    print(f"Total price: ${order1.calculate_total():.2f}")
    print("Orders for user:", [o.id for o in user1.view_orders()])


if __name__ == "__main__":
    main()
