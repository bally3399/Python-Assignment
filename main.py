from diary import Diary
from user import User


class Main:
    def __init__(self):
        self.user = User()
        self.diary = Diary("username", "password")

    def display(self):
        print("********************************")
        print("Welcome to my Diary")
        print("1.Create Entry\n 2.Unlock\n 3.Lock\n 4.Check if Dairy is locked\n 5.Find Entry\n 6.Delete Entry\n "
              "7.Update\n 8.Exit App")
        print("********************************")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.create_diary()
        elif choice == "2":
            self.create_entry()
        elif choice == "3":
            self.unlock()
        elif choice == "4":
            self.lock()
        elif choice == "5":
            self.check_if_diary_is_locked()
        elif choice == "6":
            self.find_entry()
        elif choice == "7":
            self.delete_entry()
        elif choice == "8":
            self.update_entry()
        elif choice == "9":
            self.exit()
        else:
            print("Enter valid choice")
        self.display()

    def create_entry(self):
        title = input("Enter title: ")
        body = input("Enter body: ")
        self.user.add_entry(title, body)
        print("Entry created successfully!!")
        self.display()

    def unlock(self):
        password = str(input("Enter your password: "))
        if self.diary.password == password:
            self.user.unlock_diary(password)
            print("You have successfully unlock dairy")
        else:
            print("Incorrect Password")
        self.display()

    def lock(self):
        password = str(input("Enter your password: "))
        if self.diary.password == password:
            self.user.lock_diary()
            print("You have successfully lock dairy")
        else:
            print("Incorrect Password")
        self.display()
        pass

    def check_if_diary_is_locked(self):
        password = str(input("Enter your password: "))
        if self.diary.password == password:
            if self.diary.is_locked():
                print("Diary is locked")
            else:
                print("Diary is unlocked")
        else:
            print("Incorrect Password")
        self.display()

    def find_entry(self):
        id_number = input("Enter your id: ")
        self.diary.find_entry(id_number)
        print("Entry found for ID: " + id_number)
        self.display()

    def delete_entry(self):
        id_number = input("Enter your id")
        self.diary.delete_entry(id_number)
        print("Entry delete successfully")
        self.display()

    def update_entry(self):
        id_number = input("Enter your id: ")
        title = str(input("Enter title: "))
        body = str(input("Enter body: "))
        self.user.update_entry(id_number, title, body)
        print("You have successfully updated your entry")
        self.display()

    def create_diary(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.user.create_diary(name, password)
        print("You have successfully create diary")
        self.display()

    def exit(self):
        print("Exit")
        return


def main():
    diary_app = Main()
    diary_app.display()


if __name__ == "__main__":
    main()
