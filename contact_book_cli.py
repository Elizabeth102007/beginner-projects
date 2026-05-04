import json
file_path = "contact book cli.json"
def load_contact():
    try:
       with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
           return[]

def save_contact(contacts):
    with open(file_path, "w") as file:
        json.dump(contacts, file)

contacts = load_contact()


def add_contact(contacts):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    while True:
         try:
            phone = input("Enter your phone number: ")
            break
         except ValueError:
                print("Please enter numbers.")
                continue

    info = {
        "name": name,
        "email": email,
        "phone": phone,
    }
    contacts.append(info)
    print("Contacts added")

def view_contact(contacts):
    if not contacts:
        print("No contacts added")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print("****************************")

def search_contact(contacts):
    name_search = input("Enter the name you want to search for: ")
    search = False
    for contact in contacts:
        if contact['name'] == name_search:
            print("Contact found")
            print(contact['name'])
            print(contact['email'])
            print(contact['phone'])
            search = True
            break
    if not search:
        print(f"{name_search} not found.")

def delete_contact(contacts):
    name_delete = input("Enter the name you want to delete: ")
    delete = False
    for contact in contacts:
        if contact['name'] == name_delete:
            contacts.remove(contact)
            print("Contact deleted")
            delete = True
            break
    if not delete:
        print(f"{name_delete} not found.")

def edit_contact(contacts):
    name_edit = input("Enter the name you want to edit: ")
    edit = False
    for contact in contacts:
        if contact['name'] == name_edit:
            field = input("Enter the field you want to edit: ")
            if field == "name":
                if field == "Name":
                    new_name = input("Enter your new name: ")
                    contact["Name"] = new_name
                    print("Name changed successfully!")
                    print(contact["Name"])
                elif field == "Phone":
                    new_phone = input("Enter your new phone number: ")
                    contact["Phone"] = new_phone
                    print("Phone changed successfully!")
                    print(contact["Phone"])
                elif field == "Email":
                    new_email = input("Enter the new email address: ")
                    contact["Email"] = new_email
                    print("Email changed successfully!")
                    edit = True
                    break
    if not edit:
       print(f"The field: {field} does not exist.")

while True:
    print("1. Add contacts")
    print("2. View contacts")
    print("3. Search for contacts")
    print("4. Delete contacts")
    print("5. Edit contacts")
    print("6. Quit")


    choice = input("Choose an option(1, 2, 3, 4, 5, 6)  : ")
    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Please check the available choices,and enter a valid one.")

# Add contacts
    if choice == "1":
        add_contact(contacts)
        save_contact(contacts)

# View contacts
    elif choice == "2":
         view_contact(contacts)

# Search contacts
    elif choice == "3":
        search_contact(contacts)

# Delete contacts
    elif choice == "4":
        delete_contact(contacts)
        save_contact(contacts)

# Edit expense
    elif choice == "5":
        edit_contact(contacts)
        save_contact(contacts)

# Quit program
    elif choice == "6":
         break

