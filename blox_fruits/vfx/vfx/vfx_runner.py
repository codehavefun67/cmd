import time

class VFXInstance:
    def __init__(self, vfx_data, anim_tag=None, loop=True):
        self.data = vfx_data
        self.type = vfx_data.get("type", "2D_SPRITE")
        self.loop = loop
        self.is_alive = True  # Để Manager biết khi nào nên xóa instance này
        
        self.last_update = time.time()
        self.elapsed_frame_time = 0.0 # Bộ tích lũy thời gian cho 2D
        
        # --- Khởi tạo cho 2D Sprite ---
        if self.type == "2D_SPRITE":
            if anim_tag and anim_tag in vfx_data['animations']:
                tag = vfx_data['animations'][anim_tag]
                self.frame_range = (tag['from'], tag['to'])
            else:
                self.frame_range = (0, len(vfx_data['frames']) - 1)
            
            self.current_frame_idx = self.frame_range[0]

        # --- Khởi tạo cho 3D Blender ---
        elif self.type == "3D_BLENDER":
            self.current_time = 0.0
            self.animation_name = anim_tag or "DefaultAction"
            # Lấy duration từ config, mặc định là 1.0 giây nếu không có
            self.duration = vfx_data.get("config", {}).get("duration", 1.0)

    def update(self):
        """Cập nhật trạng thái VFX"""
        if not self.is_alive:
            return

        now = time.time()
        delta = now - self.last_update
        self.last_update = now

        if self.type == "2D_SPRITE":
            self._update_2d(delta)
        elif self.type == "3D_BLENDER":
            self._update_3d(delta)

    def _update_2d(self, delta):
        self.elapsed_frame_time += delta
        frame_info = self.data['frames'][self.current_frame_idx]
        
        if self.elapsed_frame_time >= frame_info['duration']:
            # Trừ đi duration để giữ lại phần thời gian thừa, giúp animation mượt hơn
            self.elapsed_frame_time -= frame_info['duration']
            self.current_frame_idx += 1
            
            # Kiểm tra xem đã hết animation chưa
            if self.current_frame_idx > self.frame_range[1]:
                if self.loop:
                    self.current_frame_idx = self.frame_range[0]
                else:
                    self.current_frame_idx = self.frame_range[1]
                    self.is_alive = False # Đánh dấu để xóa

    def _update_3d(self, delta):
        self.current_time += delta
        if self.current_time >= self.duration:
            if self.loop:
                self.current_time = 0.0
            else:
                self.current_time = self.duration
                self.is_alive = False

    def get_render_data(self):
        """Trả về dữ liệu để Renderer của ông sử dụng"""
        if self.type == "2D_SPRITE":
            return {
                "type": "2D",
                "rect": self.data['frames'][self.current_frame_idx]['rect'],
                "texture": self.data['texture_path'],
                "is_alive": self.is_alive
            }
        else:
            return {
                "type": "3D",
                "file": self.data['source_path'],
                "time": self.current_time,
                "action": self.animation_name,
                "is_alive": self.is_alive
            }