from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all)

item_one = Item("MyItem", 750)
item_one.name = "OtherItem"
print(item_one.read_only_name)


phone_one = Phone("Nokia", 500, 5, 1)
print(Phone.all)
