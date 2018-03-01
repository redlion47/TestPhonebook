import unittest

from phonebook import Phonebook


class PhonebookTestCase(unittest.TestCase):

    def test_add_contacts(self):
        phonebook = Phonebook()
        response = phonebook.add_contacts("My Name", "0716908410")
        self.assertEqual(response["message"], "contact successfully added")

    def test_view_contacts(self):
        pass

    def test_delete_contacts(self):
        pass

    def test_edit_contacts(self):
        pass

if __name__ == '__main__':
    unittest.main()
