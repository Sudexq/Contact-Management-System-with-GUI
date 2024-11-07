class ContactManager:
    def __init__(self):
        self.contacts = []  # holding list of contacts

    # 1. Add Contact
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully!")

    # 2. View All Contacts
    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts to display")
            return
        print("\n--- Contact List ---")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {index}: ")  # Indicates the order of the item in the list.
            print(contact)  # Each item in the list is represented sequentially.

    # 3. Search Contact
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return str(contact)  # Bulunan kişinin bilgisini döndür
        return None  # Kişi bulunamadıysa None döndür

    # 4. Delete Contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)  # remove contact from contact list
                print(f"\nContact '{name}' deleted successfully!")
                return
            else:
                print(f"The contact named '{name}' is not on the list.")

    # 5. Sort Contacts
    def sort_contacts(self):
        # will be alphabetically sorted
        contact_list = self.contacts

        n = len(contact_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if contact_list[j].name > contact_list[j + 1].name:
                    contact_list[j], contact_list[j + 1] = contact_list[j + 1], contact_list[j]

        print("\nContacts sorted alphabetically by name.\n")


# NOTES
# The f in the print(f"") statement comes from a feature called f-string.
# F-strings are a practical way to embed variables and expressions within a string,
# used in Python 3.6 and later.

# Thanks to enumerate, it becomes easier to see which element is in which order,
# especially when accessing the elements of a list.
