# Trevon McKenzie
# 1880601

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        print("ADD ITEM TO CART")
        item_purchase = ItemToPurchase()
        item_purchase.item_name = input("Enter the item name\n")
        item_purchase.item_description = input("Enter the item description\n")
        item_purchase.item_price = float(input("Enter the item price\n"))
        item_purchase.item_quantity = int(input("Enter the item quantity\n"))
        self.cart_items.append(item_purchase.item_name)
        self.cart_items.append(item_purchase.item_price)
        self.cart_items.append(item_purchase.item_quantity)
        self.cart_items.append(item_purchase.item_description)



    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove:\n")
        self.cart_items.remove(item_name)

    def modify_item(self):
        print("CHANGE ITEM QUANTITY")
        item_to_change = input("Enter the item name:\n")
        new_quantity = input("Enter the new quantity:\n")
        for item in self.cart_items:
            if item == item_to_change:
                self.item_quantity = new_quantity
        else:
            print("Item not found in cart. Nothing modified.")


    def get_num_items_in_cart(self):
        item_count = 0
        for item in self.cart_items:
            item_count += item.item_quantity
            print(item_count)

    def get_cost_of_carts(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
            return total_cost

    def print_total(self):
        self.get_cost_of_carts()

    def print_shopping_cart(self):
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}\n".format(customer_name, current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        go_to_item = ItemToPurchase()
        for item in self.cart_items:
            go_to_item.print_item_cost()


    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}\n".format(customer_name, current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))

def print_menu():
    print("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit")



customer_name = input("Enter customer's name:\n")
current_date = input("Enter today's date:\n\n")
print("Customer name: {}".format(customer_name))
print("Today's date: {}\n".format(current_date))
print_menu()
print()

go_time = ShoppingCart(customer_name, current_date)

entered_character = input("Choose an option:\n")
while entered_character != 'q':
    go_time = ShoppingCart()
    if entered_character == 'r':
        go_time.remove_item()
    if entered_character == 'c':
        go_time.modify_item()
    if entered_character == 'i':
        go_time.print_descriptions()
    if entered_character == 'o':
        go_time.print_shopping_cart()
    entered_character = input("Choose an option:\n")





'''
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
print('Total: ${:.0f}'.format(go_time1.item_quantity * go_time1.item_price + go_time2.item_quantity * go_time2.item_price))'''
