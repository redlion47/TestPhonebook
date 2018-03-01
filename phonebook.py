
class Phonebook:

    def __init__(self):
        self.phonebook = {}

    def add_contact(self, name, contacts):
        self.phonebook[name] = contacts
        return {"message": "Contact successfully added!!"}

    def view_contact(self, name):
        return self.phonebook[name]

    def delete_contact(self, name):
        del self.phonebook[name]
        return {"message": "Contact successfully deleted!!"}
