// Kişi ekleme işlevi
async function addContact() {
    const name = document.getElementById("name").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;

    if (name && phone && email) {
        await eel.add_contact(name, phone, email)();
        alert(`${name} added successfully.`);
    } else {
        alert("Please fill all spaces!");
    }
}

// Kişileri görüntüleme işlevi
async function viewContacts() {
    contactList.innerHTML="<h3>Arama Sonucu</h3>"
    const contacts = await eel.get_contacts()();
    const contactList = document.getElementById("contactList");
    contactList.innerHTML = "";  // Listeyi temizle

    contacts.forEach(contact => {
        const contactDiv = document.createElement("div");
        contactDiv.textContent = contact;

        // Silme düğmesi
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.onclick = () => deleteContact(contact.split('\n')[0].split(': ')[1]);  // İsmi alma
        contactDiv.appendChild(deleteButton);

        contactList.appendChild(contactDiv);
    });
}

// Kişi silme işlevi
async function deleteContact(name) {
    if (name) {
        await eel.delete_contact(name)();
        alert(`${name} deleted successfully.`);
        viewContacts();  // Listeyi güncelle
    }
}

// Kişileri sıralama işlevi
async function sortContacts() {
    await eel.sort_contacts()();
    alert("Kişiler alfabetik olarak sıralandı.");
    viewContacts();  // Listeyi güncelle
}

// Kişi arama işlevi
async function searchContact() {
    const name = document.getElementById("searchName").value;
    if (name) {
        const result = await eel.search_contact(name)();
        
        const searchResultDiv = document.getElementById("searchResult");
        searchResultDiv.innerHTML = "";  // Arama sonucunu temizle

        searchResultDiv.innerHTML="<h3>Arama Sonucu</h3>"
        if (result) {
            searchResultDiv.textContent = `Bulunan kişi:\n${result}`;
        } else {
            searchResultDiv.textContent = "Kişi bulunamadı.";
        }
    } else {
        alert("Lütfen aramak istediğiniz ismi girin!");
    }
}