class Hobbit:
    def __init__(self, name, disposition = "homebody", age = 0, height = "short"):
        self.name = name
        self.disposition = disposition
        self.age = age
        self.height = height

    def celebrate_birthday(self):
        self.age += 1

    def is_adult(self):
        if self.age <= 32:
            return False
        else:
            return True

    def is_old(self):
        if self.age >= 101:
            return True
        else:
            return False

    def has_ring(self):
        if self.name == "Frodo":
            return True
        else:
            return False

    def is_short(self):
        return self.height
