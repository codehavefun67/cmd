from bleak import BleakClient as Client
class test_connect:
    def __init__(self):
        pass
    async def test_connect(self):
            self.write_to_console(f"[SYSTEM] Attempting to connect to {self.target_device_addr}...")
            try:
                async with Client(self.target_device_addr, timeout=10.0) as client:
                    if client.is_connected:
                        self.write_to_console(f"[SUCCESS] Connected to {self.target_device_addr}")
                    else:
                        self.write_to_console("[FAILED] Connection failed.")
            except Exception as e:
                self.write_to_console(f"[ERROR] Connection error: {e}")
