import unittest

from phonebook import Phonebook


class PhonebookAddTestCase(unittest.TestCase):

    def setUp(self):
        phonebook = Phonebook()
        self.contact1 = phonebook.add_contact

    def test_add_contact(self):
        resp = self.contact1("My Name", "0716908410")
        self.assertEqual(resp["message"], "Contact successfully added!!")

    def test_add_contact_wrong_number(self):
        resp = self.contact1
        self.assertRaises(ValueError, resp, "My Name", "07169084dy")

    def test_add_empty_contact(self):
        resp = self.contact1
        self.assertRaises(ValueError, resp, " ", "0716908432")

    def test_add_empty_number_contact(self):
        resp = self.contact1
        self.assertRaises(ValueError, resp, "Denis ", " ")


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
        self.contact = self.phonebook.add_contact("Redlion", "0715846586")

    def test_edit_contact_number(self):
        resp = self.phonebook.edit_contact("Redlion", "0754681222")
        self.assertNotEqual(resp, "0715846586")

    def test_edit_contact_name(self):
        resp = self.phonebook.edit_contact("Redlion", "Isaac")
        self.assertEqual(resp, None)


class PhonebookDeleteTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        self.contact = self.phonebook.add_contact("Redlion", "0715846586")

    def test_delete_contact(self):
        resp = self.phonebook.delete_contact("Redlion")
        self.assertEqual(resp["message"], "Contact successfully deleted!!")

    def test_view_contact_deleted(self):
        self.phonebook.delete_contact("Redlion")
        resp = self.phonebook.view_contact("Redlion")
        self.assertEqual(resp["message"], "The contact is missing!!")


if __name__ == '__main__':
    unittest.main()
