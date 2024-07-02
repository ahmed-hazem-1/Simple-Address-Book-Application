'''
Simple address book application
Made by Ahmed Hazem 6/29/2024
'''

print("Welcome to our E-Book \n")
book = {}

print("Write 'add' to add a new contact.")
print("Write 'delete' to delete a contact by name.")
print("Write 'name', 'phone', or 'email' to display each.")
print("Write 'all' to display all contacts.")
print("Write 'exit' to end the program.")

def add_contact():
    name = input("Please enter the Name: ")
    phone = input("Please enter the Phone Number: ")
    email = input("Please enter the Email: ")
    book[name] = {"Phone": phone, "Email": email}
    print("New contact added successfully.\n")

def delete_contact():
    name = input("Please enter the Name of the contact to delete: ")
    if name in book:
        del book[name]
        print(f"Contact {name} deleted successfully.\n")
    else:
        print("Contact not found.\n")

def display_book(key):
    if not book:
        print("The Book is empty.\n")
    else:
        for name, details in book.items():
            print(f"{name}: {details[key]}")
        print()

def display_all():
    if not book:
        print("The Book is empty.\n")
    else:
        for name, details in book.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
        print()

while True:
    command = input("\nEnter your command: ").strip().lower()

    if command == "exit":
        print("Exiting the program.")
        break

    elif command == "add":
        add_contact()

    elif command == "delete":
        delete_contact()

    elif command == "name":
        if not book:
            print("The Book is empty.\n")
        else:
            for name in book:
                print(f"Name: {name}")
        print()

    elif command in ["phone", "email"]:
        display_book(command.capitalize())

    elif command == "all":
        display_all()

    else:
        print("Invalid command. Please try again.")
