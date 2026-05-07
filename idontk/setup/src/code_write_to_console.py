import tkinter.scrolledtext as code_mainConsole
class write_console:
    def __init__(self):
        pass
    def write_to_console(self, text):
        code_mainConsole.config(state="normal")
        code_mainConsole.insert("end", text + "\n")
        code_mainConsole.config(state="disabled")
        code_mainConsole.see("end")
