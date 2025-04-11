class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price

    def get_info(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"
