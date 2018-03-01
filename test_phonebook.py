import unittest

from phonebook import Phonebook


class PhonebookTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        pass

    def test_add_contact(self):
        resp = self.phonebook.add_contact("My Name", "0716908410")
        self.assertEqual(resp["message"], "Contact successfully added!!")

    def test_view_contact(self):
        self.phonebook.add_contact("Redlion", "0715846586")
        resp = self.phonebook.view_contact("Redlion")
        self.assertEqual(resp, "0715846586")

    def test_delete_contact(self):
        self.phonebook.add_contact("Redlion", "0715846586")
        resp = self.phonebook.delete_contact("Redlion")
        self.assertEqual(resp["message"], "Contact successfully deleted!!")
        resp2 = self.phonebook.view_contact("Redlion")
        self.assertEqual(resp2["message"], "The contanct you \
            are looking for is missing!!")

    def test_edit_contact(self):
        pass

if __name__ == '__main__':
    unittest.main()
