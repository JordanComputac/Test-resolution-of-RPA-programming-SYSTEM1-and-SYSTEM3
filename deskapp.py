import time
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from dotenv import load_dotenv
import os


class DeskAPP:
    def __init__(self):
        
        load_dotenv()
        path_system3 = os.getenv("PATH_SYSTEM3")
        self.app = Application().start(cmd_line=path_system3)
        time.sleep(2)
          

    def close(self):
        
        self.app.ACMESystem3.Exit.click()


'''if __name__ == "__main__":
    desk_app = DeskAPP()'''
    

