class Wizard:
    def __init__(self, name, bearded = True):
        self.name = name
        self.bearded = bearded
        self.rested = True
        self.spell_counter = 0
        
    def is_bearded(self):
        return self.bearded

    def incantation(self, string):
        return f"sudo {string}"

    def is_rested(self):
        return self.rested

    def cast(self):
        self.spell_counter += 1
        if self.spell_counter >= 3:
            self.rested = False
        return "MAGIC MISSILE!"
         
