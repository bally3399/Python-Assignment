def main():
    exit_program = False
    while not exit_program:
        print("1. Add Contact\n2. Search by Name\n3. Delete Contact\n4. Display Contacts\n5. Dial Contact\n6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            search_by_name()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            display_contacts()
        elif choice == 5:
            dial_contact()
        elif choice == 6:
            exit_program = True
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")


def add_contact():
    phone_number = input("Enter phone number: ")
    name = input("Enter name: ")
    contacts[name] = phone_number
        if len(phone_number) > 13:
        print("Invalid number.")
        return
    print(f"contact {name} added successfully")

def search_by_name():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Search Results:")
        print(contacts[name])
    else:
        print("Contact not found!\n")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in the phonebook.")

def dial_contact():
    name = input("Enter name to dial: ")
    if name in contacts:
        print(f"Dialing {name} - {contacts[name]}")
    else:
        print(f"Contact '{name}' not found in the phonebook.")
def display_contacts():
    if contacts:
        print("Contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}")
            print(f"{phone_number}")
    else:
        print("No contacts available.")
contacts = {}
main()


