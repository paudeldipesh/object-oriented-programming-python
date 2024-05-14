import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        # Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    # Property decorator is read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long")
        else:
            self.__name = value

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
