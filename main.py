from contact import Contact

def main():
    print("Contact Manager Application")

    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input ("Enter phone number: ")

    contact = Contact(name, email, phone)

    print("\nContact Created:")
    print(contact.display_contact())

if __name__ == "__main__":
    main()