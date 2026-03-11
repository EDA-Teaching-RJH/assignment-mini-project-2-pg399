import csv

def save_contact (contact):
    with open("contacts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([contact.name, contact.email, contact.phone])