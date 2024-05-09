class Item:
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=1):
        # Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate


item_one = Item("Phone", 100, 5)
print(item_one.calculate_total_price())

item_one.apply_discount()
print(item_one.price)

item_two = Item("Laptop", 1000)
print(item_two.calculate_total_price())

item_two.pay_rate = 0.7
item_two.apply_discount()
print(item_two.price)
