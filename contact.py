import re

class Contact:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def validate_email(self):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, self.email)

    def display_contact(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

