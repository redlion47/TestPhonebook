import unittest

from phonebook import Phonebook


class PhonebookTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        pass

    def test_add_contacts(self):
        resp = self.phonebook.add_contacts("My Name", "0716908410")
        self.assertEqual(resp["message"], "contact successfully added")

    def test_view_contacts(self):
        self.phonebook.add_contacts("Redlion", "0715846586")
        resp = self.phonebook.view_contacts("Redlion")
        self.assertEqual(resp, "0715846586")

    def test_delete_contacts(self):
        pass

    def test_edit_contacts(self):
        pass

if __name__ == '__main__':
    unittest.main()
