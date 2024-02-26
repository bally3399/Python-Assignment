from oop2.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        new_diary = Diary(username, password)
        self.diaries.append(new_diary)

    def get_length(self):
        return self.diaries
        pass

    def find_by_user_name(self, username):
        for diary in self.diaries:
            if diary.user_name == username:
                return diary

    def remove(self, username, password):
        diary = self.find_by_user_name(username)
        if diary is not None and diary.user_name == username and diary.password == password:
            self.diaries.remove(diary)
        pass

