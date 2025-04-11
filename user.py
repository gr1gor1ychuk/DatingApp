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

    def add_order(self, order):
        self.orders.append(order)
