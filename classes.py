class Item:
    def calculate_total_price(self, x, y):
        return x * y


item_one = Item()
item_one.name = "Phone"
item_one.price = 100
item_one.quantity = 5
print(item_one.calculate_total_price(item_one.price, item_one.quantity))

item_two = Item()
item_two.name = "Laptop"
item_two.price = 1000
item_two.quantity = 3
print(item_two.calculate_total_price(item_two.price, item_two.quantity))

random_string = "dipesh"
print(random_string.upper())

# Defining a method in a class
