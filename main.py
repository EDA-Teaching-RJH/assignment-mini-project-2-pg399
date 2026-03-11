from contact import Contact

def main():
    print("Contact Manager Application")

    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input ("Enter phone number: ")

    contact = Contact(name, email, phone)

    if contact.validate_email():
     print("\nContact Created:")
     print(contact.display_contact())
    else:
        print("Invalid email format. Contact not created. ")

if __name__ == "__main__":
    main()