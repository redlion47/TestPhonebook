
class Phonebook:

    def __init__(self):
        self.phonebook = {}

    def add_contact(self, name, contact):

        if contact.isdigit() and (name or name.strip()):
            self.phonebook[name] = contact
            return {"message": "Contact successfully added!!"}

        else:
            raise ValueError

    def view_contact(self, name):
        view = self.phonebook.get(name, "Empty")
        if view == "Empty":
            return {"message": "The contact is missing!!"}

        return self.phonebook[name]

    def edit_contact(self, name, contact):
        if contact.isdigit():
            self.phonebook[name] = contact
            return self.phonebook[name]
        else:
            self.phonebook[contact] = self.phonebook[name]
            del self.phonebook[name]

            return self.phonebook.get("name")

    def delete_contact(self, name):
        del self.phonebook[name]
        return {"message": "Contact successfully deleted!!"}
