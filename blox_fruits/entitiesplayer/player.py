from ..core_game.game_state import States, Roles
from ..core_game.admin import Admin
 


class Player:
    def __init__(self, name, role=Roles.PLAYER):
        self.name = name
        self.role = role
        self.level = 1
        self.is_flying = False
        self.is_dashing = False
        self.normal_Speed = 10
        self.dashing_speed = 50
        self.flying_Speed = 90
        self.dash_timer = 1

        
        # Chỉ số (Stats)
        self.stats = {"hp": 100, "energy": 100, "fruit_mastery": 1}
        self.max_speed = 100
        self.max_hp = self.stats["hp"] * 10
        self.current_hp = self.max_hp
        self.max_energy = self.stats["energy"] * 10
        self.current_energy = self.max_energy
        self.current_speed = self.max_speed
        # Trạng thái
        self.state = States.IDLE
        self.is_in_combat = False
        self.combat_timer = 0
        
        # Hệ thống đi kèm
        self.admin_sys = Admin(self)

    def update(self, dt):
        # Giảm timer combat
        if self.combat_timer > 0:
            self.combat_timer -= dt
        else:
            self.is_in_combat = False

        # Tự động hồi phục
        multiplier = 1.0 if self.is_in_combat else 2.5
        if self.current_hp < self.max_hp:
            self.current_hp += (self.max_hp * 0.01 * multiplier) * dt
        if self.current_energy < self.max_energy:
            self.current_energy += (self.max_energy * 0.03 * multiplier) * dt
            
        # Đảm bảo không vượt quá Max
        self.current_hp = min(self.current_hp, self.max_hp)
        self.current_energy = min(self.current_energy, self.max_energy)

        current_speed = self.flying_Speed if self.is_flying else self.normal_Speed
        self.current_speed = current_speed
    def take_damage(self, amount):
        self.hp -= amount
        print(f"[System] Player consumed {amount} damage. The HP left is {max(0, self.hp)} HP.")
        if self.hp <= 0:
            print(f"[System] A player named {self.name} has died.")
    
    def start_dash(self):
        if not self.is_dashing:
            self.is_dashing = True
            self.dash_duration = self.dash_timer
            