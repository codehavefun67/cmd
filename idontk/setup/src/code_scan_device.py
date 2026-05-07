from bleak import BleakScanner as Scanner

async def scan_device(self):
        self.write_to_console("[SYSTEM] Scanning (please wait 5s)...")
        if not self.check_bluetooth_state():
            self.write_to_console("[ERROR] Bluetooth service (bthserv) is NOT running.")
            return

        try:
            devices = await Scanner.discover(timeout=5.0)
            if devices:
                self.write_to_console("FOUND DEVICES:")
                for device in devices:
                    self.write_to_console(f" > {device}")
            else:
                self.write_to_console("[SYSTEM] No devices found.")
        except Exception as e:
            self.write_to_console(f"[ERROR] Scan failed: {e}")