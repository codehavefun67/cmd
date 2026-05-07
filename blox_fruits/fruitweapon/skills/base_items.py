class BaseItem:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.cooldowns = {"Z": 0, "X": 0, "C": 0, "V": 0}

    def skill_z(self): pass
    def skill_x(self): pass
    def skill_c(self): pass
    def skill_v(self): pass

    def update_cooldowns(self, dt):
        for key in self.cooldowns:
            if self.cooldowns[key] > 0:
                self.cooldowns[key] -= dt
