import time
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from dotenv import load_dotenv
import os
from data import DataManager

class DeskAPP:
    def __init__(self):
        

        load_dotenv()
        path_system3 = os.getenv("PATH_SYSTEM3")
        self.email = os.getenv("EMAIL")
        self.passw = os.getenv("PASSW")
        
        self.app = Application().start(cmd_line=path_system3)
        time.sleep(2)
        data_man = DataManager()

    def close(self):
        
        self.app.ACMESystem3.Exit.click()
    
    def login(self):

        self.app.ACMESystem3["Username:Edit"].type_keys(self.email)
        self.app.ACMESystem3["Password:Edit"].type_keys(self.passw)
        
        self.app.ACMESystem3.Login.click()

        
        

    def search_client(self):
        self.app.ACMESystem3.set_focus()
        send_keys('%')
        send_keys('{RIGHT}')
        send_keys('{RIGHT}')
        send_keys('{DOWN}')
        send_keys('{DOWN}')
        send_keys('{RIGHT}')
        send_keys('{DOWN}')
        send_keys('~')

        time.sleep(5)

        self.app.ACMESystem3.set_focus()

        breakpoint()
        '''self.app.ACMESystem3.menu_item(u'&Clients').click()
        self.app.ACMESystem3.child_window(title="menuStrip1", auto_id="menuStrip1", control_type="System.Windows.Forms.MenuStrip").menu_item(u'&Clients').click()



        app_menu = self.app.ACMESystem3.child_window(title="Application", control_type="MenuBar")
        app_menu.child_window(title="Help").expand()


        help_menu = self.app.ACMESystem3.child_window(title="Help", control_type="Menu")
        help_menu.child_window(title="Clients").click_input()

        self.app.ACMESystem3.child_window(title="Menu Bar").set_focus()
'''
        


#self.app.ACMESystem3.print_control_identifiers()

if __name__ == "__main__":
    desk_app = DeskAPP()
    desk_app.login()
    time.sleep(10)
    desk_app.search_client()
    

