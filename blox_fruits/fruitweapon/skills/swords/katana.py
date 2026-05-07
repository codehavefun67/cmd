from fruitweapon.skills.base_items import BaseItem
from blox_fruits.core_game.admin import Admin
from blox_fruits.entitiesplayer.player import Player

class Katana(BaseItem):
    def skill_z(self):
        player = self.owner
        admin = Admin(player=player)
        cost = 20 
        cooldown_time = 3 # Chiêu Z hồi trong 3 giây

        # 1. KIỂM TRA HỒI CHIÊU (Bỏ qua nếu là Admin đang bật OP)
        if not admin.is_op_fun and self.cooldowns["Z"] > 0:
            print(f"⏳ Chiêu Z đang hồi! Còn {round(self.cooldowns['Z'], 1)}s")
            return 0
        else:
            pass
        # 2. KIỂM TRA NĂNG LƯỢNG
        # (Admin OP thì không tốn năng lượng)
        if admin.is_op_fun or player.current_energy >= cost:
            damage = player.stats['sword_mastery'] * 1.5
            
            # Trừ năng lượng và đặt Cooldown nếu không phải Admin OP
            if not admin.is_op_fun:
                player.current_energy -= cost
                self.cooldowns["Z"] = cooldown_time 
            
            player.is_in_combat = True
            player.combat_timer = 5 
            
            print(f"🚀 {player.name} dùng kỹ năng Z! Gây {damage} sát thương.")
            return damage
        else:
            print(f"❌ Không đủ năng lượng!")
            return 0
    
    def skill_x(self):
        player = self.owner 
        admin = player.admin_sys # Gọi hệ thống Admin của bro
        cost = 20 
        cooldown_time = 3 # Chiêu Z hồi trong 3 giây

        # 1. KIỂM TRA HỒI CHIÊU (Bỏ qua nếu là Admin đang bật OP)
        if not admin.is_op_fun and self.cooldowns["Z"] > 0:
            print(f"⏳ Chiêu X đang hồi! Còn {round(self.cooldowns['X'], 1)}s")
            return 0
        else:
            pass
        # 2. KIỂM TRA NĂNG LƯỢNG
        # (Admin OP thì không tốn năng lượng)
        if admin.is_op_fun or player.current_energy >= cost:
            damage = player.stats['sword_mastery'] * 1.5
            
            # Trừ năng lượng và đặt Cooldown nếu không phải Admin OP
            if not admin.is_op_fun:
                player.current_energy -= cost
                self.cooldowns["X"] = cooldown_time 
            
            player.is_in_combat = True
            player.combat_timer = 5 
            
            print(f"🚀 {player.name} dùng kỹ năng X! Gây {damage} sát thương.")
            return damage
        else:
            print(f"❌ Không đủ năng lượng!")
            return 0