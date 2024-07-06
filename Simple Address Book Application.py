'''
Simple address book application
Made by Ahmed Hazem 6/29/2024
Upgraded by FurqanHun 7/6/2024
'''

import uuid

print("Welcome to our E-Book \n")
book = {}

print("Write 'add' to add a new contact.")
print("Write 'delete' to delete a contact by ID.")
print("Write 'name', 'phone', or 'email' to display each.")
print("Write 'all' to display all contacts.")
print("Write 'exit' to end the program.")

def add_contact():
    uid = str(uuid.uuid4())
    name = input("Please enter the Name: ")
    phone = input("Please enter the Phone Number: ")
    email = input("Please enter the Email: ")
    book[uid] = {"Name": name, "Phone": phone, "Email": email}
    print(f"New contact added successfully with ID: {uid}\n")

def delete_contact():
    uid = input("Please enter the ID of the contact to delete: ")
    if uid in book:
        del book[uid]
        print(f"Contact with ID {uid} deleted successfully.\n")
    else:
        print("Contact not found.\n")

def display_book(key):
    if not book:
        print("The Book is empty.\n")
    else:
        for uid, details in book.items():
            print(f"ID: {uid}, {key}: {details[key]}")
        print()

def display_all():
    if not book:
        print("The Book is empty.\n")
    else:
        for uid, details in book.items():
            print(f"ID: {uid}, Name: {details['Name']}, Phone: {details['Phone']}, Email: {details['Email']}")
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
            for uid, details in book.items():
                print(f"ID: {uid}, Name: {details['Name']}")
        print()

    elif command in ["phone", "email"]:
        display_book(command.capitalize())

    elif command == "all":
        display_all()

    else:
        print("Invalid command. Please try again.")
