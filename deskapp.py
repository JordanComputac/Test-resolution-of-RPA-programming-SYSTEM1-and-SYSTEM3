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
        self.email = os.getenv("EMAIL")
        self.passw = os.getenv("PASSW")
        self.app = Application().start(cmd_line=path_system3).connect(title ="ACME System 3")
        time.sleep(2)
          

    def close(self):
        
        self.app.ACMESystem3.Exit.click()
    
    def login(self):

        self.app.ACMESystem3["Username:Edit"].type_keys(self.email)
        self.app.ACMESystem3["Password:Edit"].type_keys(self.passw)
        self.app.ACMESystem3.Login.click()
    
    def search_client(self):
        breakpoint()
        self.app.ACMESystem3.menu_item(u'&Clients').click()
        


#self.app.ACMESystem3.print_control_identifiers()

'''if __name__ == "__main__":
    desk_app = DeskAPP()'''
    

