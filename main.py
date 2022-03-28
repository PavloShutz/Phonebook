import json
from pathlib import Path


class PhoneBook:

    def __init__(self, phone_number, first_name, last_name, location):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.email = f"{self.first_name}_{self.last_name}.{self.location}@{self.location}.com"

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, phone: {self.phone_number}, "\
            f"location: {self.location}, email: {self.email}"

    def load_data(self):
        path = Path('phonebook.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        return [data, path]

    def write_data(self, new_data):
        data = self.load_data()[0]
        data['info'].append(new_data)
        path = self.load_data()[1]
        path.write_text(json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False), encoding='utf-8')

    def add_contact(self):
        data = {
            'Phone number': self.phone_number,
            'Name': f"{self.first_name} {self.last_name}",
            'Location': self.location,
            'Email': f"{self.email}"
        }
        self.write_data(data)

    def collect_users(self):
        contacts = []
        data = self.load_data()[0]
        return [contacts, data]

    def search_by_location(self, location):
        data = self.collect_users()[1]
        contacts = self.collect_users()[0]
        for user_info in data['info']:
            if user_info['Location'] == location:
                contacts.append(user_info['Name'])
        return 'Users in this location: ' + ', '.join([user for user in contacts])

    def search_by_email(self, email):
        data = self.collect_users()[1]
        contacts = self.collect_users()[0]
        for user_info in data['info']:
            if user_info['Email'] == email:
                contacts.append(user_info['Name'])
        return 'Users by this email: ' + ', '.join([user for user in contacts])

    def amount_of_contacts(self):
        return f"Amount of contacts: {len(self.collect_users()[1]['info'])}"

    def delete_contact(self, user_name):
        data = self.load_data()[0]
        for item in data['info']:
            if item['Name'] == user_name:
                data['info'].pop(data['info'].index(item))
        path = self.load_data()[1]
        path.write_text(json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False), encoding='utf-8')
        return "Contact deleted!"
    
    def change_contact(self, phone_number, first_name, last_name, location):
        self.delete_contact(f"{self.first_name}")
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.email = f"{self.first_name}_{self.last_name}.{self.location}@{self.location}.com"
        self.add_contact()
