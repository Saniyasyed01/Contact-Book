class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        """ Allow the user to add a new contact. """
        print("\nAdding New Contact:")
        name = input("Enter full name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print("\nContact added successfully!")

    def view_contacts(self):
        """ Display all saved contacts. """
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self):
        """ Search for a contact by name or phone number. """
        search_term = input("\nEnter name or phone number to search: ")
        results = [contact for contact in self.contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]

        if results:
            print("\n--- Search Results ---")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("\nNo contacts found.")

    def update_contact(self):
        """ Update an existing contact. """
        self.view_contacts()
        try:
            idx = int(input("\nEnter the contact number to update: ")) - 1
            if idx < 0 or idx >= len(self.contacts):
                print("\nInvalid contact number.")
                return

            print("\nLeave a field empty if you do not want to update it.")
            name = input(f"Enter new name (current: {self.contacts[idx]['name']}): ")
            phone = input(f"Enter new phone (current: {self.contacts[idx]['phone']}): ")
            email = input(f"Enter new email (current: {self.contacts[idx]['email']}): ")
            address = input(f"Enter new address (current: {self.contacts[idx]['address']}): ")

            if name: self.contacts[idx]['name'] = name
            if phone: self.contacts[idx]['phone'] = phone
            if email: self.contacts[idx]['email'] = email
            if address: self.contacts[idx]['address'] = address

            print("\nContact updated successfully!")
        except ValueError:
            print("\nInvalid input. Please try again.")

    def delete_contact(self):
        """ Delete a contact by index. """
        self.view_contacts()
        try:
            idx = int(input("\nEnter the contact number to delete: ")) - 1
            if idx < 0 or idx >= len(self.contacts):
                print("\nInvalid contact number.")
                return

            del self.contacts[idx]
            print("\nContact deleted successfully!")
        except ValueError:
            print("\nInvalid input. Please try again.")

    def display_menu(self):
        """ Display the main menu and handle user input. """
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("\nExiting the Contact Book. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.display_menu()
