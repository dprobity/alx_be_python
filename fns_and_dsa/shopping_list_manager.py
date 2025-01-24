def display_menu():
    """Displays the menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  

    while True:
        display_menu()  # Show the menu to the user
        choice = input("Enter your choice: ")  # Take the user's input

        if choice == '1':
            # Prompt for and add an item to the list
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
            print(f"Item '{item_to_add}' added to the shopping list.")
        
        elif choice == '2':
            # Prompt for and remove an item from the list
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Item '{item_to_remove}' removed from the shopping list.")
            else:
                print(f"Item '{item_to_remove}' not found in the shopping list.")
        
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
