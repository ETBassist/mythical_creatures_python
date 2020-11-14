class Centaur:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.crank_counter = 0
        self.standing = True

    def shoot(self):
        self.crank_counter += 1
        if self.crank_counter >= 3 or self.is_laying():
            response = 'NO!'
        else:
            response = 'Twang!!!'
        return response

    def run(self):
        self.crank_counter += 1
        if self.crank_counter >= 3 or self.is_laying():
            response = 'NO!'
        else:
            response = "Clop clop clop clop!!!"
        return response

    def is_cranky(self):
        return self.crank_counter >= 3

    def is_standing(self):
        return self.standing

    def is_laying(self):
        return not self.standing

    def sleep(self):
        if self.is_standing():
            return 'NO!'
        self.crank_counter = 0
        return None

    def lay_down(self):
        self.standing = False

    def stand_up(self):
        self.standing = True

    def drink_potion(self):
        if not self.is_cranky() and self.is_standing():
            return "Now I'm sick"
        if self.is_standing():
            self.crank_counter = 0
        return "Can't, I'm laying"
