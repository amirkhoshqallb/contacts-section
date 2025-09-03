import json
import os

# Global contacts list
contacts = []

# Load contacts from file
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

# Save contacts to file
def save_contacts():
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)

# Add a new contact
def add_contact():
    name = input("ENTER NAME: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    number = input("ENTER NUMBER: ").strip()
    if not number.isdigit():
        print("PLEASE ENTER A VALID NUMBER!")
        return
    contact = {"name": name, "number": number}
    contacts.append(contact)
    save_contacts()
    print(f"Contact {name} added successfully!")

# Show all contacts
def show_contacts():
    if not contacts:
        print("EMPTY")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['number']}")

# Search for a contact by name or number
def search_contact():
    query = input("ENTER NAME OR NUMBER: ").lower().strip()
    found = [c for c in contacts if query in c['name'].lower() or query in c['number']]
    if found:
        for contact in found:
            print(f"{contact['name']} - {contact['number']}")
    else:
        print("NOTHING FOUND")

# Delete a contact
def delete_contact():
    show_contacts()
    if not contacts:
        return
    try:
        index = int(input("ENTER NUMBER OF CONTACT: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts()
            print(f"{deleted_contact['name']} DELETED")
        else:
            print("INVALID CONTACT NUMBER!")
    except ValueError:
        print("ENTER CORRECT NUMBER!")

# Main menu
def main():
    load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        try:
            choice = int(input("SELECT AN OPTION: "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                show_contacts()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                print("BYE BYE!")
                break
            else:
                print("ENTER CORRECT NUMBER!")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")

if __name__ == "__main__":
    main()
        

