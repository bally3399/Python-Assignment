from oop2.entry import Entry


class Diary:
    def __init__(self, user_name, password):
        self._user_name = user_name
        self._password = password
        self.is_locked = True
        self.entries = []
        self.counter = 101

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, username):
        self._user_name = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def un_locked(self, pin):
        if self.password == pin:
            self.is_locked = False

    def is_locked(self):
        return self.is_locked

    def create_entry(self, title, body):
        new_entry = Entry(self.generate_id_entry(), title, body)
        self.entries.append(new_entry)
        return new_entry
        pass

    def generate_id_entry(self):
        return self.counter

    def get_entries(self):
        return self.entries

    def lock(self):
        self.is_locked = True
        return self.is_locked

    def find_entry(self, id):
        for entry in self.entries:
            if entry.id_number == id:
                return entry
        return None

    def delete_entry(self, id_number):
        entry = self.find_entry(id_number)
        self.entries.remove(entry)

    def update_entry(self, id_number, title, body):
        for entry in self.entries:
            if entry.id_number == id_number:
                entry._title = title
                entry._body = body






