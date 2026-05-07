from bleak import BleakClient as Client
class pair:
    def __init__(self):
        pass
    async def pair(self):
        """Hàm pair đã được sửa lỗi gọi phương thức instance"""
        self.write_to_console(f"[SYSTEM] Attempting to pair with {self.target_device_addr}...")
        try:
            async with Client(self.target_device_addr) as cli:
                if cli.is_connected:
                    self.write_to_console(f"[SYSTEM] Connected. Sending pair request...")
                    # Gọi phương thức pair của đối tượng client (cli)
                    success = await cli.pair()
                    if success:
                        self.write_to_console(f"[SUCCESS] Device {self.target_device_addr} paired successfully!")
                    else:
                        self.write_to_console(f"[INFO] Pairing returned False (might already be paired).")
                else:
                    self.write_to_console("[ERROR] Could not connect to device for pairing.")
        except Exception as e:
            self.write_to_console(f"[ERROR] Pairing process failed: {e}")