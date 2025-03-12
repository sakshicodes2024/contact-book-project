from contact import Contact
class ContactBook:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,contact):
        self.contacts.append(contact)
    def display_all_contacts(self):
        for contact in self.contacts():
            print("--------------")
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                return contact
        return None