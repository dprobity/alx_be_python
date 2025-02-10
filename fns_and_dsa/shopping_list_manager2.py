shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    update_item = input("please adda an item from the list of items you have viewd before")
    shopping_list.append(update_item)
    return shopping_list

def remove_item():
    deleted_item = input("please remove an item from your cart")
    shopping_list.remove(deleted_item)
    return shopping_list

def view_list():
    for item in shopping_list:
        print(item)



x = 0
while x != 4:
    display_menu()
    x = int(input(("Enter the correspondinng number to take action")))
    x = x

match x:
    case 1:
         add_item()
    case 2:
        remove_item()
    case 3:
        view_list()
    case _:
        if x>4:
            print("This is an invalid ")
            print("type 4 to exit or select from the options")
            display_menu()






