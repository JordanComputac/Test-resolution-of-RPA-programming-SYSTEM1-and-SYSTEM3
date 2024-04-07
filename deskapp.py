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

        #self.app = Application().start(cmd_line=path_system3)
        self.app = Application(backend="uia").start(cmd_line=path_system3)
        #self.app = Application(backend="uia").connect(title = 'ACME System3', timeout = 10)

        time.sleep(2)
        self.data_man = DataManager()

    def close(self):
        
        self.app.ACMESystem3.Exit.click()
    
    def login(self):

        self.app.ACMESystem3["Username:Edit"].type_keys(self.email)
        self.app.ACMESystem3["Password:Edit"].type_keys(self.passw)
        self.app.ACMESystem3.Login.click()
        

        
        

    def search_client(self):
        
        
        file = self.data_man.files_list_csv(1)
        client_id = self.data_man.get_client_request_id(file)
        client_name = self.data_man.get_client_name(file)
        client_check_number = self.data_man.get_check_number(file)
        date = self.data_man.get_date(file)
        

        #tratamento da data
        year, month, day = date.split('-')
        
        year = int(year)
        month = int(month)
        day = int(day)


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

        self.app.ACMESystem3.Includeinactiveclients.click()
        #comando abaixo retorna muitos items
        #self.app.ACMESystem3["TextBox1:Edit"].type_keys("whatareel")

        search_form_field = self.app.ACMESystem3.child_window(auto_id="textBox1", control_type="Edit").wrapper_object()
        search_form_field.type_keys("^a")  
        search_form_field.type_keys("{BACKSPACE}")
        search_form_field.type_keys(client_id, with_spaces = True)
        btn_search = self.app.ACMESystem3.child_window(title="Search", auto_id="button1", control_type="Button").wrapper_object()

        

        btn_search.click()
        
        
        
        #self.app.ACMESystem3.set_focus()

        popup = self.app.window(found_index=0)

        

        send_keys('{TAB}')
        send_keys('{TAB}')
        send_keys('{TAB}')
        send_keys('{DOWN}')

        #self.app.ACMESystem3.KeshiaPentecost.click_input()
        #self.app.ACMESystem3.client_name.click_input(button='left', double=True)
        client_name_str = client_name.replace(' ', '')
        command_line = f"self.app.ACMESystem3.{client_name_str}.click_input(button='left', double=True)"
        eval(command_line)
        
        

        

        try:
            
            btn_client_check = self.app.ACMESystem3.child_window(title="Client Checks", auto_id="button2", control_type="Button").wrapper_object()
            btn_client_check.click_input()
            time.sleep(5)
            print("Busca por cliente por ID encontrou o cliente com sucesso, procurando por checks")
        except:
            print("Busca por cliente por ID não retornou resultados")
        

        field_check_number = self.app.ACMESystem3.child_window(title="Status", auto_id="textBox2", control_type="Edit")
        field_check_number.type_keys("^a")
        field_check_number.type_keys("{BACKSPACE}")
        field_check_number.type_keys(client_check_number, with_spaces = True)

        send_keys('{TAB}')
        send_keys(f'{day}')
        send_keys('{RIGHT}')
        send_keys(f'{month}')
        send_keys('{RIGHT}')
        send_keys(f'{year}')
        send_keys('{RIGHT}')

        status_field = self.app.ACMESystem3.child_window(auto_id="comboBox1", control_type="ComboBox").wrapper_object()
        status_field.type_keys("Processed")

        send_keys('{TAB}')
        send_keys(' ')
        
        
        breakpoint()

        
        
        #date_field = self.app.ACMESystem3.child_window(title="Search", auto_id="button1", control_type="Button").wrapper_object()



    def search_client2(self):
        
        clients_tab = self.app.ACMESystem3.child_window(title="Clients", control_type="MenuItem").wrapper_object()
        self.app.ACMESystem3.set_focus()
        clients_tab.click_input()

        
        
        search_for_client_tab = self.app.ACMESystem3.child_window(title="Search For Client", control_type="MenuItem").wrapper_object()
        #search_for_client_tab = self.app.ACMESystem3.child_window(title="Search For Client", control_type="MenuItem").wrapper_object()
        search_for_client_tab.click_input()
        breakpoint()


#self.app.ACMESystem3.print_control_identifiers()

'''if __name__ == "__main__":
    desk_app = DeskAPP()
    desk_app.login()
    time.sleep(10)
    desk_app.search_client()'''
    

