import tkinter as code_UI
import tkinter.scrolledtext as code_mainConsole
version = "10.2.2010213 Build 1.1"
def __init__(self, root):
        self.root = root
        self.root.title("Command Prompt")
        self.root.geometry("875x400")
        self.root.configure(bg="black")
        
        # Địa chỉ mặc định (bạn có thể thay đổi qua lệnh connect nếu muốn)
        self.target_device_addr = "86:C6:2F:91:3E:84" 
        
        # Entry for commands
        self.entry = code_UI.Entry(master=self.root, bg="#1e1e1e", fg="white", 
                                    insertbackground="white", font=("Consolas", 11))
        self.entry.pack(pady=5, padx=10, fill="x")
        self.entry.bind("<Return>", self.process_command)

        # Console widget
        self.code_mainConsole = code_mainConsole.ScrolledText(master=self.root, bg="black", 
                                                              fg="#FFFFFF", font=("Consolas", 11),
                                                              state="disabled")
        self.code_mainConsole.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.write_to_console(f"Developer CMD (Windows x Ubuntu) Version {version}\n(c)No Corporation. All rights reserved.\n")
