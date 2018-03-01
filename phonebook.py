
class Phonebook:

    def __init__(self):
        self.phonebook = {}

    def add_contacts(self, name, contacts):
        self.phonebook[name] = contacts
        return {"message": "contact successfully added"}

    def view_contacts(self, name):
        pass
