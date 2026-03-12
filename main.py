from tabulate import tabulate
from contact import Contact
from file_manager import save_contact, load_contacts

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice =="1":

           name = input("Enter name: ")
           email = input("Enter email: ")
           phone = input ("Enter phone number: ")

           contact = Contact(name, email, phone)

           if contact.validate_email():
              save_contact(contact)
              print("Contact saved succesfully.")
           else:
          
              print("Invalid email format.")

        elif choice == "2":

           contacts = load_contacts()

           if contacts:
              print("\nSaved Contacts:")
              for c in contacts:
                  print(f"Name: {c[0]}, Email: {c[1]}, Phone: {c[2]}")

           else:
                print("No contacts found.")

        
        elif choice == "3":

            search_name = input("Enter name to search: ").lower()
            contacts = load_contacts()

            found = False

            for c in contacts:
                if search_name in c[0].lower():
                    print(f"Name: {c[0]}, Email: {c[1]}, Phone: {c[2]}")
                    found = True
            if not found:
                print("No matching contact found. ")

        elif choice == "4":
            print("Exiting program. ")
            break
        
        else:
            print("Invalid option. ")

if __name__ =="__main__":
    main()
    
         