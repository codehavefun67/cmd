import os
import json
import shutil
import platform

class VFXManager:
    def __init__(self, assets_path="./assets/vfx"):
        self.assets_path = assets_path
        self.vfx_cache = {}
        
        # Tự động tìm và cấu hình Blender ngay khi khởi tạo manager
        self.blender_bin_path = self._find_blender_executable()
        self._setup_blender_environment()

    @staticmethod
    def _find_blender_executable():
        """Tìm đường dẫn đến thư mục chứa blender.exe"""
        # 1. Kiểm tra trong PATH hệ thống trước
        blender_in_path = shutil.which("blender")
        if blender_in_path:
            return os.path.dirname(blender_in_path)

        # 2. Các đường dẫn mặc định trên Windows
        if platform.system() == "Windows":
            common_paths = [
                r"C:\Program Files\Blender Foundation",
                r"C:\Program Files (x86)\Blender Foundation",
                os.path.expanduser(r"~\AppData\Local\Programs\Blender Foundation")
            ]

            for base_path in common_paths:
                if os.path.exists(base_path):
                    # Quét các thư mục con (Blender 4.2, Blender 3.6, v.v.)
                    for folder in os.listdir(base_path):
                        full_path = os.path.join(base_path, folder)
                        if "Blender" in folder and os.path.isdir(full_path):
                            if os.path.exists(os.path.join(full_path, "blender.exe")):
                                return full_path
        return None

    def _setup_blender_environment(self):
        """Tiêm đường dẫn Blender vào môi trường để Ursina/Panda3D có thể gọi"""
        if self.blender_bin_path:
            if self.blender_bin_path not in os.environ["PATH"]:
                os.environ["PATH"] += os.pathsep + self.blender_bin_path
            print(f"🚀 VFXManager: Đã kết nối Blender tại: {self.blender_bin_path}")
        else:
            print("⚠️ VFXManager Warning: Không tìm thấy Blender. File .blend sẽ không thể convert!")

    def load_vfx(self, vfx_name):
        """Load VFX dựa trên tên, tự động nhận diện 2D hoặc 3D"""
        if vfx_name in self.vfx_cache:
            return self.vfx_cache[vfx_name]

        blend_path = os.path.join(self.assets_path, f"{vfx_name}.blend")
        json_path = os.path.join(self.assets_path, f"{vfx_name}.json")
        img_path = os.path.join(self.assets_path, f"{vfx_name}.png")

        # Ưu tiên 3D (.blend)
        if os.path.exists(blend_path):
            return self._load_blender_vfx(vfx_name, blend_path)

        # Ngược lại load 2D (Aseprite)
        if os.path.exists(json_path) and os.path.exists(img_path):
            return self._load_aseprite_vfx(vfx_name, json_path, img_path)

        print(f"❌ Lỗi: Không tìm thấy file cho VFX '{vfx_name}' tại {self.assets_path}")
        return None

    def _load_blender_vfx(self, vfx_name, file_path):
        """Xử lý metadata cho file Blender"""
        # Fix lỗi: file_path là đường dẫn đến file .blend, không phải thư mục Blender
        vfx_data = {
            "type": "3D_BLENDER",
            "source_path": file_path,
            "status": "ready_to_render" if self.blender_bin_path else "missing_blender",
            "config": {
                "engine": "EEVEE",
                "is_baked": False
            }
        }
        
        self.vfx_cache[vfx_name] = vfx_data
        print(f"📦 Đã cache VFX 3D: {vfx_name}")
        return vfx_data

    def _load_aseprite_vfx(self, vfx_name, json_path, img_path):
        """Xử lý dữ liệu sprite 2D từ Aseprite"""
        with open(json_path, 'r') as f:
            data = json.load(f)

        vfx_data = {
            "type": "2D_SPRITE",
            "texture_path": img_path,
            "frames": [],
            "animations": {}
        }

        for frame in data['frames']:
            vfx_data["frames"].append({
                "rect": (frame['frame']['x'], frame['frame']['y'], frame['frame']['w'], frame['frame']['h']),
                "duration": frame['duration'] / 1000.0
            })

        if 'meta' in data and 'frameTags' in data['meta']:
            for tag in data['meta']['frameTags']:
                vfx_data["animations"][tag['name']] = {
                    "from": tag['from'], "to": tag['to'], "direction": tag['direction']
                }

        self.vfx_cache[vfx_name] = vfx_data
        print(f"✅ Đã cache VFX 2D: {vfx_name}")
        return vfx_data