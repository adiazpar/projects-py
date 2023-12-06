"""
Homework 3 Exercise 3
Name: Alejandro Diaz
Due Date: 10/06/23

Exercise 3:
Imagine you have this inventory in a store:

    Item                Number of item
    Hand sanitizer      10
    Soap                6
    Kleenex             22
    Lotion              16
    Razors              12

1. Save the inventory in a data structure.

2. Write a function printInventory(inventory) that will take any possible inventory as the
input, and display it in a nice format (like the printPicnic() function in format.py given in
class).

3. Write a function addItem(inventory, item) to add one new item to the data structure each
time it is called. For example, calling addItem(inventory, ‘Advil’) for the first time will
create an item Advil with a count of 1; calling it the second time will increase Advil’s
count to 2, and so on. Calling addItem(inventory, ‘Lotion’) for the first time will increase
Lotion’s count from 16 to 17.

4. Write a function deleteItem(inventory, item) to delete items (but don’t delete a whole
item group). It has the opposite effect of addItem(inventory, item). For example, calling
deleteItem(inventory, ‘Soap’) for the first time will reduce Soap’s count to 5, and so on,
until the item’s count reaches 0. When the count is already 0, print an error message that
the item cannot be deleted any further.
"""


# Function to print inventory in a neat format:
def print_inventory(inv, l_width, r_width):
    print("\n" + 'INVENTORY ITEMS'.center(l_width + r_width, '-'))
    for k, v in inv.items():
        print(k.ljust(l_width, '.') + str(v).rjust(r_width))


# Function to add an item to the inventory:
def add_item(inv, item):
    # Check to see if added item is in the inventory:
    inv[item] = inv.get(item, 0) + 1

    print_inventory(inv, 20, 6)
    print("Added 1 " + item + " to your inventory...")

    """""
    This does the same thing as:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
    """


# Function to delete an item from the inventory:
def delete_item(inv, item):
    if inv.get(item) <= 0:
        print("\nERROR: There are 0 " + item + "(s) in your inventory... \nItem not deleted")
        inv[item] = 0
    else:
        inv[item] -= 1

        print_inventory(inv, 20, 6)
        print("Deleted 1 " + item + " from your inventory...")


# Main function for the driver code:
if __name__ == "__main__":

    # Initializing the inventory with the given data:
    inventory = {"Hand Sanitizer": 10, "Soap": 6, "Kleenex": 22, "Lotion": 16, "Razors": 12}
    print_inventory(inventory, 20, 6)

    # Adding an item to the Inventory:
    add_item(inventory, "Advil")
    # Deleting an item from the Inventory:
    delete_item(inventory, "Soap")
