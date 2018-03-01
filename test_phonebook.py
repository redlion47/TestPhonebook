import unittest

from phonebook import Phonebook


class PhonebookAddTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        self.contact1 = self.phonebook.add_contact("My Name", "0716908410")
        pass

    def test_add_contact(self):
        resp = self.contact1
        self.assertEqual(resp["message"], "Contact successfully added!!")


class PhonebookViewTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        self.contact = self.phonebook.add_contact("Redlion", "0715846586")

    def test_view_contact(self):
        resp = self.phonebook.view_contact("Redlion")
        self.assertEqual(resp, "0715846586")


class PhonebookEditTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_edit_contact(self):
        pass


class PhonebookDeleteTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_delete_contact(self):
        self.phonebook.add_contact("Redlion", "0715846586")
        resp = self.phonebook.delete_contact("Redlion")
        self.assertEqual(resp["message"], "Contact successfully deleted!!")
        resp2 = self.phonebook.view_contact("Redlion")
        self.assertEqual(resp2["message"], "The contact is missing!!")


if __name__ == '__main__':
    unittest.main()
