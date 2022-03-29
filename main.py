from phonebook import PhoneBook

contact_book = PhoneBook(None, None, None, None)
text = """
Phonebook.
1) Add a contact;
2) Search by location;
3) Search by email;
4) Delete contact;
5) Change contact;
6) Show all contacts;
7) Show amount of contacts.
"""


def get_user_input():
    phone_number = int(input("Your phone number: "))
    name = input("Contact name: ")
    location = input("Location: ")
    return [phone_number, name.split(' '), location]


while True:
    print(text)
    user_input = input("Choose option >>> ")
    if user_input == '1':
        phone_number, name, location = get_user_input()
        new_contact = PhoneBook(phone_number, name[0], name[1], location)
        print(new_contact.add_contact())
    elif user_input == '2':
        location = input("Input location >>> ")
        search = contact_book.search_by_location(location)
        print(search) if search else print("There is no contact by this location :(")
