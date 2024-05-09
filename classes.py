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
        return float(self.price * self.quantity)


item_one = Item("Phone", 100, 5)
print(item_one.calculate_total_price())

item_two = Item("Laptop", 1000)
print(item_two.calculate_total_price())


print(Item.__dict__)  # All the attributes for Class level
print(item_one.__dict__)  # All the attributes for instance level
print(Item.pay_rate)
print(item_two.pay_rate)
