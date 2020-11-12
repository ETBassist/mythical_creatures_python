class Werewolf:
    def __init__(self, name, location = "Somewhere", human_state = True, hungry = False):
        self.name = name
        self.location = location
        self.human_state = human_state
        self.hungry = hungry


    def is_human(self):
        return self.human_state
    
    def change(self):
        self.human_state = not self.human_state
        if not self.human_state:
            self.hungry = True

    def is_wolf(self):
        return not self.human_state

    def is_hungry(self):
        return self.hungry

    def consume(self, target):
        if self.is_wolf():
            target.status = "Dead"
            self.hungry = False
        else:
            return "No one was consumed"

class Victim:
    def __init__(self):
        self.status = "Alive"

