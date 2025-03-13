# Contact manager application
contacts = []


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

   
    if any(contact[0] == name for contact in contacts):
        print("Error: Contact with this name already exists!")
        return

    contacts.append((name, phone, email))
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nList of Contacts:")
    index=1
    for contact in contacts:
        name,phone,email = contact
        print(index,".",name,"-",phone,"-",email)
        index+=1


def search_contact():
    search_name = input("Enter name to search: ").strip()
    found = False

    for name, phone, email in contacts:
        if name.lower() == search_name.lower():
            print(f"Contact Found: {name} - {phone} - {email}")
            found = True
            break

    if not found:
        print("Contact not found!")


def update_contact():
    search_name = input("Enter name to update: ")
    index=0
    for contact in contacts:
        name,phone,email=contact
        if name.lower() == search_name.lower():
            new_phone = input("Enter new phone number: ")
            contacts[index] = (name, new_phone, email)  
            print("Contact updated successfully!")
            return
        index+=1
    print("Contact not found!")


def delete_contact():
    search_name = input("Enter name to delete: ")
    global contacts
    new_contacts = [contact for contact in contacts if contact[0].lower() != search_name.lower()]
    
    if len(new_contacts) == len(contacts):
        print("Contact not found!")
    else:
        contacts = new_contacts
        print("Contact deleted successfully!")


while True:
    print("\nWelcome to Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-6.")
