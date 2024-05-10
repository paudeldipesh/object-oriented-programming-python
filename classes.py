class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        # Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'


item_one = Item("Phone", 100, 5)
item_two = Item("Laptop", 1000)
item_three = Item("Cable", 10, 5)
item_four = Item("Mouse", 50, 5)
item_five = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:
    print(
        f"The price of a {instance.name} is ${instance.price} and there are {instance.quantity} in stock."
    )
