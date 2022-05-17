"""Phonebook class realization"""

import json
from typing import Optional

from data import GetData

file_data = GetData()


class PhoneBook:
    """Simple implementation of phonebook class"""

    def __init__(self, phone_number: Optional[int],
                 first_name: Optional[str], last_name: Optional[str],
                 location: Optional[str]):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.email = \
            f"{self.first_name}_{self.last_name}" \
            f".{self.location}@{self.location}.com"

    def __str__(self) -> str:
        return f"Name: {self.first_name} " \
               f"{self.last_name}, phone: {self.phone_number}, " \
               f"location: {self.location}, email: {self.email}"

    def add_contact(self) -> str:
        """Adds a new contact to JSON-file"""
        contact_data = {
            'Phone number': self.phone_number,
            'Name': f"{self.first_name} {self.last_name}",
            'Location': self.location,
            'Email': f"{self.email}"
        }
        file_data.write_data(contact_data)
        return "Contact added!"

    def _collect_users(self) -> list:
        """Returns contacts and data from JSON-file"""
        contacts: list = []
        data = file_data.load_data()[0]
        return [contacts, data]

    amount_of_contacts = "Amount of contacts: " \
                         + str(len(file_data.load_data()[0]['info']))

    def search_by_location(self, location: str) -> str:
        """Returns users found by location"""
        data = self._collect_users()[1]['info']
        contacts = self._collect_users()[0]
        for user_info in data:
            if user_info['Location'] == location:
                contacts.append(user_info['Name'])
        return 'Users in this location: ' + \
               ', '.join([user for user in contacts])

    def search_by_email(self, email: str) -> str:
        """Returns users found by this email"""
        data = self._collect_users()[1]['info']
        contacts = self._collect_users()[0]
        for user_info in data:
            if user_info['Email'] == email:
                contacts.append(user_info['Name'])
        return 'Users by this email: ' + ', '.join([user for user in contacts])

    def delete_contact(self, user_name: str) -> str:
        """Deletes contact from phonebook"""
        data = file_data.load_data()[0]
        for item in data['info']:
            if item['Name'] == user_name:
                data['info'].pop(data['info'].index(item))
        path = file_data.load_data()[1]
        path.write_text(json.dumps(data, sort_keys=False,
                                   indent=4, ensure_ascii=False),
                        encoding='utf-8')
        return "Contact deleted!"

    def change_contact(self, phone_number: Optional[int],
                       first_name: Optional[str], last_name: Optional[str],
                       location: Optional[str]):
        """Changes contact data"""
        self.delete_contact(f"{self.first_name}")
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.email = \
            f"{self.first_name}_{self.last_name}." \
            f"{self.location}@{self.location}.com"
        self.add_contact()

    def show_all_users(self):
        data = file_data.load_data()[0]
        contacts = self._collect_users()[0]
        for item in data['info']:
            contacts.append(item)
        return f"Users: \n {[user for user in contacts]}"
