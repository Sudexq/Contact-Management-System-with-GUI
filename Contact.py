# each contact has same attributes
# name
# phone
# email

class Contact:
    def __init__(self, name, phone, email):
        self.name = name.strip().title()  # starting word with a uppercase
        self.phone = phone.strip()
        self.email = email.strip().lower()  # turning lowercase

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


# NOTES
# string.strip(): it removes leading and trailing whitespace

# what is? def __str__(self):
# for example
# person = Contact("ali", "555 555 555" , "ali@gmail.com")
# print(person)
# output:
"""
Name: Ali
Phone: 555 555 555
Email: ali@gmail.com
"""
