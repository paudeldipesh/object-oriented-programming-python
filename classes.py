import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(number):
        # We will count out the floats that are point zero
        # For example: 5.0, 10.0
        if isinstance(number, float):
            # Count out the floats that are point zero
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

    def __repr__(self):
        return (
            f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'
        )


Item.instantiate_from_csv()

print(Item.all)


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=1, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones > 0
        ), f"Broken phones {broken_phones} is not greater than zero"

        # Assign to self object
        self.broken_phones = broken_phones


phone_one = Phone("Nokia", 500, 5, 1)
print(Phone.all)
