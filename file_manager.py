
import csv

def save_contact (contact):
    with open("contacts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([contact.name, contact.email, contact.phone])

def load_contacts():
    contacts = []

    try:
        with open ("contacts.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print("No contacts file not found yet. ")
    return contacts