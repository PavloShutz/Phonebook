"""Phonebook class realization"""
import json
from data import GetData

file_data = GetData()


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

    def add_contact(self):
        contact_data = {
            'Phone number': self.phone_number,
            'Name': f"{self.first_name} {self.last_name}",
            'Location': self.location,
            'Email': f"{self.email}"
        }
        file_data.write_data(contact_data)
        return "Contact added!"

    def _collect_users(self):
        contacts = []
        data = file_data.load_data()[0]
        return [contacts, data]

    amount_of_contacts = "Amount of contacts: " + str(len(file_data.load_data()[0]['info']))

    def search_by_location(self, location):
        data = self._collect_users()[1]['info']
        contacts = self._collect_users()[0]
        for user_info in data:
            if user_info['Location'] == location:
                contacts.append(user_info['Name'])
        return 'Users in this location: ' + ', '.join([user for user in contacts])

    def search_by_email(self, email):
        data = self._collect_users()[1]['info']
        contacts = self._collect_users()[0]
        for user_info in data:
            if user_info['Email'] == email:
                contacts.append(user_info['Name'])
        return 'Users by this email: ' + ', '.join([user for user in contacts])

    def delete_contact(self, user_name):
        data = file_data.load_data()[0]
        for item in data['info']:
            if item['Name'] == user_name:
                data['info'].pop(data['info'].index(item))
        path = file_data.load_data()[1]
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
