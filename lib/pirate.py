class Pirate:
    def __init__(self, name, job = "Scallywag"):
        self.name = name
        self.job = job
        self.heinous_acts = 0
        self.booty = 0

    def is_cursed(self):
        return self.heinous_acts >= 3

    def commit_heinous_act(self):
        self.heinous_acts += 1

    def rob_ship(self):
        self.booty += 100
