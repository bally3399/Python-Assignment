import unittest
from phone import Phone
class TestContactFunction(unittest.TestCase):
    def setUp(self):
        self.phone = Phone()

    def test_add_contact(self):
        self.phone.add_contact("John", "08105795528")
        self.assertEqual(self.phone.contacts["John"], "08105795528")

    def test_delete_contact(self):
        self.phone.add_contact("jane", "08106795528")
        self.phone.delete_contact("john")
        self.assertNotIn("john", self.phone.contacts, "Contact not deleted successfully.")

    def test_display_contacts(self):
        self.phone.add_contact("Ruth", "1111111111")
        self.phone.add_contact("Esther", "2222222222")
        contacts = self.phone.display_contacts()
        self.assertEqual(len(contacts), 2, "Incorrect number of contacts.")

    def test_dial_contact(self):
        self.phone.add_contact("Bally", "08105795528")
        dial_result = self.phone.dial_contact("Bally")
        expected_result = "Dialing Bally: 08105795528"
        self.assertEqual(dial_result, expected_result, f"Expected: {expected_result}, {dial_result}")

if __name__ == '__main__':
    unittest.main()

