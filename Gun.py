class Gun:
    def __init__(self):
        self.is_empty = True
        self.bullet = 0

    def chamber_is_empty(self):
        return self.is_empty

    def add_bullet(self):
        self.bullet += 1
        self.is_empty = False
        return self.bullet

    def shoot(self):
        if self.bullet > 0:
            self.bullet -= 1
            if self.bullet == 0:
                self.is_empty = True
            return self.bullet
        else:
            return None

    def load_bullet(self):
        self.bullet = 5
        self.is_empty = False
        return self.bullet




