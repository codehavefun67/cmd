import subprocess
class check_bluetooth_state:
    def __init__(self):
        pass
    def check_bluetooth_state(self):
            try:
                output = subprocess.check_output("sc query bthserv", shell=True).decode("utf-8")
                return "RUNNING" in output
            except:
                return False