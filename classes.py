from item import Item
from keyboard import Keyboard
from phone import Phone

Item.instantiate_from_csv()

print(Item.all)

item_one = Item("New Item", 750)
print(item_one.name)
# Setting an attribute
item_one.name = "Other Item"
# Getting an attribute
print(item_one.name)
item_one.apply_increment(0.2)  # polymorphism in action
item_one.apply_discount()
print(item_one.price)

item_two = Keyboard("New Keyboard", 800, 7)
item_two.apply_discount()  # polymorphism in action
print(item_two.price)

item_three = Phone("New Phone", 12000, 3, 1)
item_three.apply_discount()  # polymorphism in action
print(item_three.price)
