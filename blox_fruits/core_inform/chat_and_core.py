"""chat_and_core is a module used for create a chat shows information about the core and the players' message.
This one need module Ursina for making the UI text. To use this, please install Ursina first. Can be used for any operating system."""

from ursina import Text
from collections import deque

class Chat_Logs:
    def __init__(self, max_lines=8):
        # 1. Khởi tạo dữ liệu trước
        self.max_lines = max_lines
        self.logs = deque(maxlen=self.max_lines)
        
        # 2. Khởi tạo UI Text (Gọn gàng và chuẩn tọa độ)
        self.ui_text = Text(
            text='',
            position=(-0.85, 0.45),
            origin=(-0.5, 0.5),
            scale=1.1, # Điều chỉnh nhẹ để cân đối
            line_height=1.2,
            background=False # Có thể set True nếu muốn có khung mờ
        )
        
        # 3. Nạp log khởi tạo (Sử dụng hàm nạp hàng loạt để tối ưu)
        initial_msgs = [
            "[System] Loaded successfully.",
            "[System] Updated for 3D VFX."
        ]
        
        for m in initial_msgs:
            self.log_message(m, refresh=False)
        self.update_display() # Chỉ vẽ lại 1 lần duy nhất sau khi nạp xong

    def log_message(self, msg, refresh=True):
        # Làm sạch chuỗi (xóa khoảng trắng và dấu xuống dòng dư thừa)
        msg = msg.strip()
        
        # Logic phân loại màu sắc chuẩn tag Ursina
        if "+" in msg:
            formatted_msg = f'<green>{msg}</green>'
        elif "!" in msg:
            formatted_msg = f'<red>{msg}</red>'
        else:
            formatted_msg = f'<white>{msg}</white>'
            
        self.logs.append(formatted_msg)
        
        if refresh:
            self.update_display()

    def update_display(self):
        # Nối các dòng log, đảm bảo không bị thừa dòng trống
        self.ui_text.text = '\n'.join(self.logs)

    def clear_logs(self):
        """Hàm bổ trợ để xóa sạch log khi cần"""
        self.logs.clear()
        self.update_display()