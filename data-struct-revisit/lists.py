
shopping_list = ["milk", "bread", "eggs"]

def show_list():
    print("\nCurrent shopping list:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")
    print()

while True:
    print("Options:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    elif choice == "3":
        show_list()

    elif choice == "4":
        print("Exiting the shopping list programme.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
# hehe
