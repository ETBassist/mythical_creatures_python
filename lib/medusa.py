class Medusa:
    def __init__(self, name):
        self.name = name
        self.statues = []

    def stare(self, target):
        target.stone = True
        self.statues.append(target)
        if len(self.statues) > 3:
            self.statues[0].stone = False
            self.statues.remove(self.statues[0])

class Person:
    def __init__(self, name):
        self.name = name
        self.stone = False

    def is_stoned(self):
        return self.stone
