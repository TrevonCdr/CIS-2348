# Trevon McKenzie
# 1880601

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))



print('Item 1')
go_time1 = ItemToPurchase()
go_time1.item_name = input("Enter the item name:\n")
go_time1.item_price = float(input("Enter the item price:\n"))
go_time1.item_quantity = int(input("Enter the item quantity:\n\n"))

print('Item 2')
go_time2 = ItemToPurchase()
go_time2.item_name = input("Enter the item name:\n")
go_time2.item_price = float(input("Enter the item price:\n"))
go_time2.item_quantity = int(input("Enter the item quantity:\n\n"))

print('TOTAL COST')
go_time1.print_item_cost()
go_time2.print_item_cost()
print()
print('Total: ${:.0f}'.format(go_time1.item_quantity * go_time1.item_price + go_time2.item_quantity * go_time2.item_price))


