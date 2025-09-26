phone_book = {}

while True:
    print("\nPhone Book Options:")
    print("1. Add a contact")
    print("2. Look up a contact")
    print("3. Delete a contact")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print(f"Added {name}: {number}")

    elif choice == "2":
        name = input("Enter name to look up: ")
        if name in phone_book:
            print(f"{name}'s number is {phone_book[name]}")
        else:
            print(f"{name} not found in phone book.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Deleted {name} from phone book.")
        else:
            print(f"{name} not found in phone book.")

    elif choice == "4":
        print("Exiting phone book.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
