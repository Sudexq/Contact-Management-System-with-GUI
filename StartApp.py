import eel
from ContactManager import ContactManager
from Contact import Contact

# Kişi yönetimi için ContactManager sınıfı örneğini oluşturuyoruz
manager = ContactManager()

# Eel ile bağlantı kuracak işlevler
@eel.expose
def add_contact(name, phone, email):
    contact = Contact(name, phone, email)
    manager.add_contact(contact)

@eel.expose
def get_contacts():
    return [str(contact) for contact in manager.contacts]

@eel.expose
def delete_contact(name):
    manager.delete_contact(name)

@eel.expose
def sort_contacts():
    manager.sort_contacts()

@eel.expose
def search_contact(name):
    return manager.search_contact(name)

# Eel’i başlat
eel.init('web')  # web klasörünü kaynak dizini olarak ayarlıyoruz
eel.start('index.html')
