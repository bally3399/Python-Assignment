from diary import Diary


class Main:
    def __init__(self):
        self.diary = Diary("username", "password")

    def display(self):
        print("********************************")
        print("Welcome to my Diary")
        print("1.Create Entry\n 2.Unlock\n 3.Lock\n 4.Check if Dairy is locked\n 5.Find Entry\n 6.Delete Entry\n "
              "7.Update\n 8.Exit App")
        print("********************************")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.create_entry()
        elif choice == "2":
            self.unlock()
        elif choice == "3":
            self.lock()
        elif choice == "4":
            self.check_if_diary_is_locked()
        elif choice == "5":
            self.find_entry()
        elif choice == "6":
            self.delete_entry()
        elif choice == 7:
            self.update_entry()
        elif choice == 8:
            self.exit()
        else:
            print("Enter valid choice")
        self.display()

    def create_entry(self):
        title = input("Enter title: ")
        body = input("Enter body: ")
        self.diary.create_entry(title, body)
        print("Entry created successfully!!")
        self.display()

    def unlock(self):
        password = str(input("Enter your password: "))
        if self.diary.password == password:
            self.diary.un_locked(password)
            print("You have successfully unlock dairy")
        else:
            print("Incorrect Password")
        self.display()

    def lock(self):
        password = str(input("Enter your password: "))
        if self.diary.password == password:
            self.diary.lock()
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
        id_number = input("Entry your id")
        title = str(input("Enter title"))
        body = str(input("Enter body"))
        self.diary.update_entry(id_number, title, body)
        print("You have successfully updated your entry")

    def exit(self):
        print("Exit")
        return


def main():
    diary_app = Main()
    diary_app.display()


if __name__ == "__main__":
    main()