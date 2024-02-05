class Phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def display_contacts(self):
        return list(self.contacts.keys())

    def dial_contact(self, name):
        if name in self.contacts:
            return f"Dialing {name}: {self.contacts[name]}"
        else:
            return f"Contact {name} not found."
