from diary import Diary


class User:
    def __init__(self):
        self.diary = Diary("username", "password")

    def create_diary(self, username, password):
        diary = Diary(username,password)
        return diary

    def lock_diary(self):
        self.diary.lock()

    def unlock_diary(self, password):
        self.diary.un_locked(password)

    def add_entry(self, title, password):
        self.diary.create_entry(title, password)

    def delete_entry(self, id_number):
        self.diary.delete_entry(id_number)

    def find_entry_by_id(self, id_number):
        return self.diary.find_entry(id_number)

    def update_entry(self,id_number, new_title, new_body):
        self.diary.update_entry(id_number,new_title,new_body)
