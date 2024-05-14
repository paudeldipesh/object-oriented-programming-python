from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all)

item_one = Item("New Item", 750)
print(item_one.name)
# Setting an attribute
item_one.name = "Other Item"
# Getting an attribute
print(item_one.name)
