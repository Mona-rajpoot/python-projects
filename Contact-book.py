#contactbook where you can add, delete, update and view contacts.
contacts = []  #contacts is a list that will store the contacts.
while True:
    print("1. Add contact \n2. View contacts \n3. Update contact \n4. Delete contact \n5. Exit")
    choice = input("Enter your choice 1-5: ")
    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts.append({"name": name, "phone": phone})  #append is used to add the contact to the list of contacts.
        print("Contact added successfully!")
    elif choice == 2:
        if not contacts:
            print("No contacts to display.")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice == 3:
        name = input("Enter the name of the contact to update: ")
        for contact in contacts:
            if contact["name"] == name:
                new_phone = input("Enter the new phone number: ")
                contact["phone"] = new_phone
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")
    elif choice == 4:
        name = input("Enter the name of the contact to delete: ")
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")