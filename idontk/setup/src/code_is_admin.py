import ctypes
class is_admin:
    def __init__(self):
        pass
    def is_admin(self):
        admin_request = ctypes.windll.shell32.IsUserAnAdmin()
        if admin_request:
            return True
        else:
            return False
