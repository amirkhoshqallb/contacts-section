

A simple Python command-line application for managing contacts. This project allows users to add, view, search, and delete contacts, with data stored persistently in a JSON file.

Features





Add Contact: Add a new contact with name and phone number.



View Contacts: Display all saved contacts with their details.



Search Contact: Search contacts by name or phone number.



Delete Contact: Remove a contact from the list.



Persistent Storage: Contacts are saved in a contacts.json file for data persistence.

Requirements





Python 3.x



No external libraries required (uses built-in json and os modules)

Installation





Clone or download this repository:

git clone https://github.com/your-username/contact-manager.git



Navigate to the project directory:

cd contact-manager

Usage





Run the program using Python:

python contact_manager.py



Follow the on-screen menu to:





Add a new contact (option 1)



View all contacts (option 2)



Search for a contact by name or number (option 3)



Delete a contact (option 4)



Exit the program (option 5)

Example

Contact Manager
1. Add Contact
2. Show Contacts
3. Search Contact
4. Delete Contact
5. Exit
SELECT AN OPTION: 1
ENTER NAME: Ali
ENTER NUMBER: 09123456789
Contact Ali added successfully!

File Structure





contact_manager.py: The main Python script for the contact manager.



contacts.json: The file where contacts are stored (created automatically).



README.md: Project documentation.



.gitignore: Ignores the contacts.json file to avoid committing sensitive data.

Future Improvements





Add support for editing existing contacts.



Implement email validation and additional contact fields.



Add sorting functionality for contacts.



Create a graphical user interface (GUI) using Tkinter or PyQt.

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bug reports.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or feedback, reach out via GitHub Issues.
