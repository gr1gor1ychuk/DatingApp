import pytest
from user import User
from product import Product
from order import Order


@pytest.fixture
def user():
    return User(1, "Alice", "alice@example.com")


@pytest.fixture
def product1():
    return Product(101, "Bike", 299.99)


@pytest.fixture
def product2():
    return Product(102, "Helmet", 49.99)


@pytest.fixture
def order(user):
    return Order(1, user)


def test_user_registration():
    print("Testing user registration...")
    user = User(1, "Alice", "alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"


def test_single_user_has_no_orders_initially():
    print("Testing single user has no orders initially...")
    user = User(1, "Alice", "alice@example.com")
    assert len(user.orders) == 0


def test_multiple_users_and_their_orders():
    print("Testing multiple users and their individual orders...")

    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com")

    product = Product(101, "Book", 10.0)

    order1 = Order(1, user1)
    order1.add_product(product)

    order2 = Order(2, user2)
    order2.add_product(product)

    assert len(user1.orders) == 1
    assert len(user2.orders) == 1
    assert user1.orders[0].user == user1
    assert user2.orders[0].user == user2


def test_add_product_to_order(order, product1):
    print("Testing adding product to order...")
    order.add_product(product1)
    assert product1 in order.products


def test_remove_product_from_order(order, product1):
    print("Testing removing product from order...")
    order.add_product(product1)
    order.remove_product(product1)
    assert product1 not in order.products


def test_calculate_total(order):
    print("Testing order total calculation...")
    product1 = Product(101, "Bike", 299.99)
    product2 = Product(102, "Helmet", 49.99)
    order.add_product(product1)
    order.add_product(product2)
    assert order.calculate_total() == 349.98


def test_product_info():
    print("Testing product info retrieval...")
    product1 = Product(101, "Bike", 299.99)
    assert product1.get_info() == "Product: Bike, Price: $299.99"


def test_multiple_orders_for_user():
    print("Testing multiple orders for a user...")
    user = User(1, "Alice", "alice@example.com")
    Order(1, user)
    Order(2, user)
    assert len(user.orders) == 2


def test_order_associated_with_user(user, order):
    print("Testing order association with user...")
    assert order in user.view_orders()


def test_remove_nonexistent_product(order, product1):
    print("Testing removal of nonexistent product...")
    order.remove_product(product1)
    assert len(order.products) == 0


def test_empty_order_total(order):
    print("Testing total price of empty order...")
    assert order.calculate_total() == 0.0


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", "test_ecommerce.py"])
