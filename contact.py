import re   # Import regex library 

# Contact class store information about a contact 
class Contact:


# Constructor that sets the name, email and phone 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# Function that checks if the email format is valid
    def validate_email(self):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, self.email)
    
# Function that returns the contact information    
    def display_contact(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

