"""Rocket Fruit :D"""
from Weapons_And_Fruit import Fruit
from BloxFruit import Player, Admin

class Rocket(Fruit):
    def skill_z(self):
        player = self.owner 
        admin = self.owner # Gọi hệ thống Admin của bro
        cost = 10 
        cooldown_time = 3 # Chiêu Z hồi trong 3 giây

        # 1. KIỂM TRA HỒI CHIÊU (Bỏ qua nếu là Admin đang bật OP)
        if not admin.is_op_fun and self.cooldown["Z"] > 0:
            print(f"⏳ Chiêu Z đang hồi! Còn {round(self.cooldown['Z'], 1)}s")
            return 0
        else:
            pass
        # 2. KIỂM TRA NĂNG LƯỢNG
        # (Admin OP thì không tốn năng lượng)
        if admin.is_op_fun or player.current_energy >= cost:
            damage = player.stats['fruit_mastery'] * 1.5
            
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
        cost = 15 
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
            damage = player.stats['fruit_mastery'] * 1.5
            
            # Trừ năng lượng và đặt Cooldown nếu không phải Admin OP
            if not admin.is_op_fun:
                player.current_energy -= cost
                self.cooldowns["X"] = cooldown_time 
            
            player.is_in_combat = True
            player.combat_timer = 5 
            
            print(f"🚀 {player.name} dùng kỹ năng Z! Gây {damage} sát thương.")
            return damage
        else:
            print(f"❌ Không đủ năng lượng!")
            return 0
    
    
    def skill_c(self):
        player = self.owner 
        admin = player.admin_sys # Gọi hệ thống Admin của bro
        cost = 20 
        cooldown_time = 3 # Chiêu Z hồi trong 3 giây

        # 1. KIỂM TRA HỒI CHIÊU (Bỏ qua nếu là Admin đang bật OP)
        if not admin.is_op_fun and self.cooldowns["Z"] > 0:
            print(f"⏳ Chiêu C đang hồi! Còn {round(self.cooldowns['C'], 1)}s")
            return 0
        else:
            pass
        # 2. KIỂM TRA NĂNG LƯỢNG
        # (Admin OP thì không tốn năng lượng)
        if admin.is_op_fun or player.current_energy >= cost:
            damage = player.stats['fruit_mastery'] * 1.5
            
            # Trừ năng lượng và đặt Cooldown nếu không phải Admin OP
            if not admin.is_op_fun:
                player.current_energy -= cost
                self.cooldowns["C"] = cooldown_time 
            
            player.is_in_combat = True
            player.combat_timer = 5 
            
            print(f"🚀 {player.name} dùng kỹ năng C! Gây {damage} sát thương.")
            return damage
        else:
            print(f"❌ Không đủ năng lượng!")
            return 0
    
    def skill_f(self):
        player = self.owner
        admin = player.admin_sys
        cost = 15  # Tốn 15 năng lượng một lần duy nhất để bật/tắt
        
        # 1. Kiểm tra Cooldown (Để tránh việc spam bật/tắt liên tục làm lag game)
        if not admin.is_op_fun and self.cooldowns["F"] > 0:
            print(f"⏳ Chờ {round(self.cooldowns['F'], 1)}s để thao tác tiếp.")
            return

        # 2. Logic Bật/Tắt (Toggle)
        if not player.is_flying:
            # --- BẮT ĐẦU BAY ---
            if admin.is_op_fun or player.current_energy >= cost:
                player.is_flying = True
                
                if not admin.is_op_fun:
                    player.current_energy -= cost
                
                # Sau khi bật xong, cho hồi chiêu ngắn để tránh bug
                self.cooldowns["F"] = 1.0 
                print(f"🚀 {player.name} đã kích hoạt động cơ phản lực! (Bay tự do)")
            else:
                print(f"❌ Cần {cost} năng lượng để cất cánh!")
        else:
            # --- TẮT BAY ---
            player.is_flying = False
            self.cooldowns["F"] = 2.0 # Hồi chiêu 2 giây sau khi tắt
            print(f"⚓ {player.name} đã tắt động cơ, đang hạ cánh.")