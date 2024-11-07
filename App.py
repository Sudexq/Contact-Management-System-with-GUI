from ContactManager import ContactManager
from Contact import Contact


# our menu
def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Sort Contacts")
    print("6. Exit")


# main function
def main():
    manager = ContactManager()  # creating manager object for managing contact list
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        # 1. Add Contact
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            contact = Contact(name, phone, email)  # creating contact object
            manager.add_contact(contact)  # adding new object to our list

        # 2. View All Contacts
        elif choice == "2":
            if manager.contacts:
                manager.view_contacts()
            else:
                print("\nThe contact list is empty!\nPlease add a contact first.")

        # 3. Search Contact
        elif choice == "3":
            if manager.contacts:
                name = input("Enter the name to search: ")
                manager.search_contact(name)
            else:
                print("\nThe contact list is empty!\nPlease add a contact first.")

        # 4. Delete Contact
        elif choice == "4":
            if manager.contacts:
                name = input("Enter the name to delete: ")
                manager.delete_contact(name)
            else:
                print("\nThe contact list is empty!\nPlease add a contact first.")

        # 5. Sort Contacts
        elif choice == "5":
            if manager.contacts:
                manager.sort_contacts()
            else:
                print("\nThe contact list is empty!\nPlease add a contact first.")

        # 6. Exit
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        # other inputs
        else:
            print("Invalid input! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

# WHAT SHOULD PROGRAM DO?
"""
1. Add Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Sort Contacts
6. Exit
"""

# NOTES
# what is if __name__ == "__main__":
# we are doing it because there are different functions
# and i don't wanna misunderstanding in my program
