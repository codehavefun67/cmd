import shlex as code_MainProcesser
import threading as thread
class CMD:
    def __init__(self):
        pass
    def process_command(self, event):
            raw_input = self.entry.get().strip()
            self.entry.delete(0, "end")
            
            if not raw_input:
                return -1

            self.write_to_console(f"user@system ~$ {raw_input}")

            try:
                # Phân tách lệnh và tham số bằng shlex
                tokens = code_MainProcesser.split(raw_input)
                cmd = tokens[0].lower()
                args = tokens[1:]

                if cmd == "scan":
                    thread.Thread(target=self.run_async_task, args=(self.scan_device(),), daemon=True).start()
                
                elif cmd == "connect":
                    # Nếu người dùng nhập 'connect <MAC>', cập nhật địa chỉ đích
                    if args:
                        self.target_device_addr = args[0]
                    thread.Thread(target=self.run_async_task, args=(self.test_connect(),), daemon=True).start()
                
                elif cmd == "pair":
                    # Gọi hàm pair đã sửa lỗi
                    thread.Thread(target=self.run_async_task, args=(self.pair(),), daemon=True).start()
                
                elif cmd == "clear":
                    self.code_mainConsole.config(state="normal")
                    self.code_mainConsole.delete(3.0, code_UI.END)
                    self.code_mainConsole.config(state="disabled")
                
                else:
                    self.write_to_console(f"'{cmd}' is not recognized as an internal or external command,\noperable program or batch file.")
            
            except Exception as e:
                self.write_to_console(f"[SHELL ERROR] {e}")