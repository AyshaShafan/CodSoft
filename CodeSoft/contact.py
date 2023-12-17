class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, 1):
                print(f"{index}. Name: {contact['name']}, Phone: {contact['phone_number']}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_query):
        found_contacts = []
        for contact in self.contacts:
            if search_query in contact['name'] or search_query in contact['phone_number']:
                found_contacts.append(contact)

        if found_contacts:
            print(f"Search results for '{search_query}':")
            for contact in found_contacts:
                print(
                    f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No matching contacts found.")

    def update_contact(self, old_name, name, phone_number, email, address):
        for contact in self.contacts:
            if contact['name'] == old_name:
                contact['name'] = name
                contact['phone_number'] = phone_number
                contact['email'] = email
                contact['address'] = address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for index, contact in enumerate(self.contacts):
            if contact['name'] == name:
                del self.contacts[index]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_query = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_query)
        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            name = input("Enter Updated Name: ")
            phone_number = input("Enter Updated Phone Number: ")
            email = input("Enter Updated Email: ")
            address = input("Enter Updated Address: ")
            contact_book.update_contact(old_name, name, phone_number, email, address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
