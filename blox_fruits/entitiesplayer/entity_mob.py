
class Mob:
    def __init__(self, name, level, x, y):
        self.name = name
        self.level = level
        self.hp = level * 50
        self.max_hp = self.hp
        self.x = x
        self.y = y

    def take_damage(self, amount):
        self.hp -= amount
        print(f"[Mob] {self.name} nhận {amount} sát thương. Còn {max(0, self.hp)} HP.")
        if self.hp <= 0:
            print(f"[Mob] {self.name} đã bị tiêu diệt!")