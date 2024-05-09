class Item:
    def __init__(self, name: str, price: float, quantity=1):
        print(f"Item name: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return float(self.price * self.quantity)


item_one = Item("Phone", 100, 5)
print(item_one.calculate_total_price())

item_two = Item("Laptop", 1000)
print(item_two.calculate_total_price())
