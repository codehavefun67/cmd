class Admin:
    def __init__(self, player):
        self.player = player
        self.is_op_fun = False # Chế độ No Cooldown & Infinite Energy
        self.is_f = False
        self.running_fast = False

    def execute_command(self, command):
        # Kiểm tra nếu role là admin mới cho dùng lệnh
        if self.player.role != "admin":
            print(f"[Hệ thống] {self.player.name} không có quyền Admin.")
            return

        if command == "/opfun":
            self.is_op_fun = not self.is_op_fun
            trang_thai = "BẬT" if self.is_op_fun else "TẮT"
            print(f"[Admin] Chế độ OP đã {trang_thai}!")
            
        elif command.startswith("/s"):
            try:
                new_level = int(command.split()[1])
                self.player.level = new_level
                print(f"[Game] Đã đặt Level của {self.player.name} thành {new_level}")
            except:
                print("[Game] Lệnh sai. VD: /s 100")
        elif command.startswith("/f"):
            try:
                new_fighting = str(command.split()[1])
                self.player.fighting = new_fighting
                print(f"[Game] Đã đặt Fighting Style của {self.player.name} thành {new_fighting}")
            except:
                print("[Game] This is not a command.")
        elif command.startswith("/kick"):
            try:
                kick_player = str(command.split()[1])
                self.player.kick = kick_player
                print(f"[Game] Đã kick player {self.player.kick}")
            except:
                print("[Game] This is not a command.")
        else:
            print("[Game] U dont have admin.")