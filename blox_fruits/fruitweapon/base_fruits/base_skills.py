"""This is a module to make any fruits in this package."""

class Fruit:
    """This one is use at making skills."""
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner # Đối tượng Player sở hữu
        self.cooldown = {"Z": 0, "X": 0, "C": 0, "V": 0, "F": 0}

    def skill_z(self): raise NotImplementedError
    def skill_x(self): raise NotImplementedError
    def skill_c(self): raise NotImplementedError
    def skill_v(self): raise NotImplementedError
    def skill_f(self): raise NotImplementedError

    def update_cooldowns(self, dt):
        # Hàm này sẽ được gọi trong vòng lặp game để giảm thời gian hồi chiêu
        for skill in self.cooldown:
            if self.cooldown[skill] > 0:
                self.cooldown[skill] -= dt
                if self.cooldown[skill] < 0:
                    self.cooldown[skill] = 0