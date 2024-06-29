'''
Simple address book application
Made by Ahmed Hazem 6/29/2024
'''


print("Welcome to our E-Book \n")
book = {"Name": None, "Phone": None, "Email": None}
book["Name"] = input("Please enter your Name: ")
book["Phone"] = input("Please enter your Phone Number: ")
book["Email"] = input("Please enter your Email: ")

print("Write 'Name', 'Phone', or 'Email' to display each.")
print("Write 'all' to display all contacts.")
print("Write 'exit' or 'Exit' to end the program.")

while True:
    command = input("\nEnter your command: ").strip()

    if command == "exit" or command == "Exit":
        print("Exiting the program.")
        break

    if command == "Name" or command == "name":
        print(f"Name: {book['Name']}")

    elif command == "Phone" or command == "phone":
        print(f"Phone: {book['Phone']}")

    elif command == "Email" or command == "email":
        print(f"Email: {book['Email']}")

    elif command == "all":
        print(f"Name: {book['Name']}")
        print(f"Phone: {book['Phone']}")
        print(f"Email: {book['Email']}")

    else:
        print("Invalid command. Please try again.")

