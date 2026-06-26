import json
file_path = "contact_book.json"

def load_contacts():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(file_path, "w") as file:
        json.dump(contacts, file, indent=2)

def add_contacts(contacts):
    name = input("Enter your name: ").lower()
    email= input("Enter your email address: ")
    phone = input("Enter your phone number: ")
           
    person = {
              "name" : name,
              "email" : email,
              "phone" : phone
              }
    
    contacts.append(person)
    print("Contact updated!")


def view_contacts(contacts):
    if not contacts:
        print("No contact added")
    else:
        for contact in contacts:
            print(f"Name: {contact['name'].capitalize()}")
            print(f"Email Address : {contact['email']}")
            print(f"Phone Number: {contact['phone']}")
            print("****************************")


def search_contacts(contacts):
    name_search = input("Enter the name you want to search for: ")
    search = False
    for contact in contacts:
        if contact['name'] == name_search.lower():
            print("Contact found")
            print(contact['name'])
            print(contact['email'])
            print(contact['phone'])
            search = True
            break
    if not search:
        print(f"{name_search} not found.")

def delete_contacts(contacts):
    name_delete = input("Enter the name you want to delete: ")
    delete = False
    for contact in contacts:
        if contact['name'] == name_delete.lower():
            contacts.remove(contact)
            print("Contact deleted")
            delete = True
            break
    if not delete:
        print(f"{name_delete} not found.")


contacts = load_contacts()
def menu():
    print("=====CONTACT BOOK====")
    print("1. Add contacts")
    print("2. View contacts")
    print("3. Search for contacts")
    print("4. Delete contacts")
    print("5. Exit")
    
def main():
    print(f"Total Contacts: {len(contacts)}")
    while True:
       menu()
       choice = input("Choose an option(1, 2, 3, 4, 5, 6)  : ")
       if choice not in ("1", "2", "3", "4", "5", "6"):
           print("Please check the available choices,and enter a valid one.")

       if choice == "1":
           add_contacts(contacts)
           save_contacts(contacts)


       elif choice == "2":
            view_contacts(contacts)


       elif choice == "3":
            search_contacts(contacts)


       elif choice == "4":
             delete_contacts(contacts)
             save_contacts(contacts)


       elif choice == "5":
         break
       
       else:
           print("Invalid choice")

if __name__ == "__main__":
    main()



