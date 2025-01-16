def show_menu():
    print('\nContact List Menu:')
    print('1. Add New Contact')
    print('2. Remove Existing Contact')
    print('3. Search for a Contact')
    print('4. View All Contacts')
    print('5. Exit Program\n')

def add_contact(contact_book):
    name = input('Enter the full name of the contact: ').strip()
    if name in contact_book:
        print(f"A contact named '{name}' already exists.")
        return
    phone = input('Enter the phone number: ').strip()
    email = input('Enter the email address: ').strip()
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' has been successfully added.")

def delete_contact(contact_book):
    name = input('Enter the full name of the contact to remove: ').strip()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' has been successfully removed.")
    else:
        print(f"No contact found with the name '{name}'.")

def search_contact(contact_book):
    name = input('Enter the full name of the contact to search for: ').strip()
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print('-' * 20)
    else:
        print(f"No contact found with the name '{name}'.")

def list_contacts(contact_book):
    if contact_book:
        print('\nSaved Contacts:')
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print('-' * 20)
    else:
        print('No contacts available to display.')

def contact_list():
    contact_book = {}

    while True:
        show_menu()
        option = input('Choose an option from the menu: ').strip()
        print('\n')

        if option == '1':
            add_contact(contact_book)
        elif option == '2':
            delete_contact(contact_book)
        elif option == '3':
            search_contact(contact_book)
        elif option == '4':
            list_contacts(contact_book)
        elif option == '5':
            print('Exiting the contact list program. Goodbye!')
            break
        else:
            print('Invalid option. Please choose a valid option (1-5).')

contact_list()

         


          
