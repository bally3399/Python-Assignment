from unittest import TestCase
from oop2.diary import Diary


class TestDiaryFunctions(TestCase):
    def setUp(self):
        self.diary = Diary("user_name", "password")

    def test_create_entry(self):
        self.diary.un_locked("password")
        self.assertFalse(self.diary.is_locked)

        self.diary.create_entry("title", "body")
        self.assertEqual(len(self.diary.get_entries()), 1)

    def test_set_up_diary(self):
        self.diary.un_locked("password")
        self.assertFalse(self.diary.is_locked)

    def test_enter_wrong_password_diary_remains_locked(self):
        self.diary.un_locked("incorrect_password")
        self.assertTrue(self.diary.is_locked)

    def test_that_diary_can_be_lock(self):
        self.diary.lock()
        self.assertTrue(self.diary.is_locked)

    def test_find_entry_by_id(self):
        self.diary.un_locked("password")
        self.assertFalse(self.diary.is_locked)

        self.diary.create_entry("title", "body")
        found_entry = self.diary.find_entry(101)
        self.assertEqual(101, found_entry.id_number)

    def test_delete_entry(self):
        self.diary.un_locked("password")
        self.assertFalse(self.diary.is_locked)

        self.diary.create_entry("title", "body")
        self.diary.find_entry(101)
        self.assertEqual(len(self.diary.get_entries()), 1)

        self.diary.delete_entry(101)
        self.assertEqual(len(self.diary.get_entries()), 0)

    def test_update_entry(self):
        self.diary.un_locked("password")
        self.assertFalse(self.diary.is_locked)

        self.diary.create_entry("title", "body")
        self.diary.update_entry(101, "new_title", "new_body")
        found_diary = self.diary.find_entry(101)
        self.assertEqual("new_title", found_diary.title)
        self.assertEqual("new_body", found_diary.body)
