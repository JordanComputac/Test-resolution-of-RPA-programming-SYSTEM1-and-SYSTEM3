import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import PyPDF2
import glob
import os
import pandas as pd
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from data import DataManager
import time




class ChromeDriverManager:
    def __init__(self):
        
        #chromedriver_path só é necessário caso chromedriver esteja em outro diretorio
        #self.chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
        
        load_dotenv()
        self.pdf_dir = os.getenv("PDF_PATH")
        self.email = os.getenv("EMAIL")
        self.passw = os.getenv("PASSW")
        self.image_dir = os.getenv("IMAGE_PATH")
        
        chrome_options = Options()
        self.data_man = DataManager()
       

        chrome_options.add_experimental_option('prefs', {
        "download.default_directory": self.pdf_dir, 
        "download.prompt_for_download": False, 
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True 
        })

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)


    def get_driver(self):
        return self.driver
    

    def search(self):

        search_bar = self.driver.find_element(By.XPATH, '//textarea[@name="q"]')        
        search_bar.send_keys("Python programming")
        search_bar.send_keys(Keys.ENTER)

        
    def login(self):
        self.driver.get("https://acme-test.uipath.com/login")
        email_fld  = self.driver.find_element(By.XPATH, '//input[@id="email"]')        
        email_fld.send_keys(self.email)
        passw_fld = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        passw_fld.send_keys(self.passw)
        btn_login = self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        
        #btn_work_items = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, '(//button[@type="button"])[3]')))
        btn_work_items = self.driver.find_element(By.XPATH, '(//button[@type="button"])[3]').click()


    def click_next(self):

        try:
            btn_next = self.driver.find_element(By.XPATH,"//a[@aria-label = 'Next »']")
            btn_next.click()
            print("Procurando por mais categorias WI2...")
            return "Procurando por mais categorias WI2..."
        except:
            print("Não foi possível mais clicar na proxima página da lista ")
            return "Não foi possível mais clicar na proxima página da lista "
            
        
    def search_check(self, archive_number):
            
            
            self.driver.get("https://acme-test.uipath.com/home")

            search_client = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Search for Check')]")
            link_search = search_client.get_attribute("href")
            self.driver.get(link_search)

            time.sleep(3)

            file = self.data_man.files_list_csv(archive_number)
            check_number = self.data_man.get_check_number(file)
            string_date = self.data_man.get_date(file)
            year, month_name, day = self.data_man.get_date_detail(string_date)

            check_number_field = self.driver.find_element(By.XPATH,"//input[@id='checkNumber']")
            check_number_field.send_keys(str(check_number))

            day_field = self.driver.find_element(By.XPATH,"//input[@id='checkDay']")
            day_field.send_keys(str(day))

            
            menu_month_dropdown = self.driver.find_element(By.XPATH,"(//button[@class='btn dropdown-toggle bs-placeholder btn-default'])[1]")
            #select = Select(menu_month_dropdown)
            menu_month_dropdown.click()            
            month_dropdown = self.driver.find_element(By.XPATH,f"//span[contains(text(), '{month_name}')]")
            month_dropdown.click()

            try:    
                menu_year_dropdown = self.driver.find_element(By.XPATH,"//button[@class='btn dropdown-toggle bs-placeholder btn-default']")
                menu_year_dropdown.click()
                year_dropdown = self.driver.find_element(By.XPATH,f"//span[contains(text(), '{year}')]")
                year_dropdown.click()

            except:
                print(f"Ano {year} inexistente no menu de dropdown")
                return "Falha em Client Search Check"

            
            btn_search = self.driver.find_element(By.XPATH,"//button[contains(text(), 'Search Check')]")
            btn_search.click()
            time.sleep(5)
            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                
                alert.accept()

                if  alert_text == "No check was found based on the criteria that you have specified.":
                    print("Nenhum Check foi encontrado com as informações fornecidas")
                    return "Nenhum Check foi encontrado com as informações fornecidas"
                else:

                    print("Alert Text:", alert_text)
            except:
                print("Não foi possível clicar em alert boxes, verificar...")
                return "Caso desconhecido, talvez tenha encontrado cliente check"
                
                    
    def submit_check(self, archive_number):
        self.driver.get("https://acme-test.uipath.com/home")
        
        search_client = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Submit Check Copy')]")
        link_search = search_client.get_attribute("href")
        self.driver.get(link_search)

        file = self.data_man.files_list_csv(archive_number)
        check_number = self.data_man.get_check_number(file)
        client_id = self.data_man.get_client_request_id(file)

        client_id_field = self.driver.find_element(By.XPATH,"//input[@id = 'workitemID']")
        client_id_field.send_keys(str(client_id))

        client_id_field = self.driver.find_element(By.XPATH,"//input[@id = 'checkNumber']")
        client_id_field.send_keys(str(check_number))

        
        img_file = file.replace('.csv', '.jpg')
        
        parent_dir = os.path.dirname(os.path.abspath(__file__))

        path_image = parent_dir+"\\images\\praialitoralprai.jpg"        
        send_image_input = self.driver.find_element(By.XPATH,"//input[@id = 'my-file-selector']")
        send_image_input.send_keys(path_image)

        
        btn_search = self.driver.find_element(By.XPATH,"//button[contains(text(), 'Upload Check Copy')]")
        btn_search.click()
        
        time.sleep(5)
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            
            alert.accept()

            if  alert_text == 'Check was uploaded':
                print("upload  de check realizado com sucesso!")
                return "upload  de check realizado com sucesso!"
            else:

                print("Alert Text:", alert_text)
        except:
            print("Não foi possível realizar upload de check, verificar...")
            return "Caso desconhecido, não foi possível realizar upload de check"
    
    def update_status(self, archive_number):
        self.driver.get("https://acme-test.uipath.com/login")
        
        btn_work_items = self.driver.find_element(By.XPATH, '(//button[@type="button"])[3]').click()

        
        file = self.data_man.files_list_csv(archive_number)
        wiid = file.replace('.csv', '')

        while True:
            
            link = self.driver.find_elements(By.XPATH,f"(//*[contains(text(),'{str(wiid)}')]//preceding-sibling::td/a)[1]")
            time.sleep(3)
            if link:
                print("Elemento - Número do cliente encontrado")
                
                break
            else: 
                next = self.click_next()
                if next == "Não foi possível mais clicar na proxima página da lista":
                    print("Após procurar em todas as listas não foi encontrado cliente")
                    break 
                else:
                    print("Procurando elemento - Número do cliente")
        
        

        #link = self.driver.find_elements(By.XPATH,"(//*[contains(text(),'99391397')]//preceding-sibling::td/a)[1]")
        
        #Rotina para baixar o documento
        original_tab = self.driver.current_window_handle
        actions = ActionChains(self.driver)
        
        time.sleep(3)
        actions.key_down(Keys.CONTROL).click(link[0]).key_up(Keys.CONTROL).perform()
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        
        
        btn_update = self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-default']")
        btn_update.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        text_area = self.driver.find_element(By.XPATH, "//textarea[@name='newComment']")
        text_area.send_keys("Check found in System 1,uploaded to client.")
        
        btn_status = text_area = self.driver.find_element(By.XPATH, "//button[@class='btn dropdown-toggle bs-placeholder btn-default']")
        btn_status.click()

        complete_dropdown = self.driver.find_element(By.XPATH,"(//*[contains(text(),'Complete')])[1]")
        complete_dropdown.click()
                
        btn_send = self.driver.find_element(By.XPATH,"//button[@id='buttonUpdate']")
        btn_send.click()

        time.sleep(5)
        try:

            alert = self.driver.switch_to.alert
            alert_text = alert.text
            
            alert.accept()

            if  alert_text == 'Work Item was updated accordingly':
                print("update realizado com sucesso!")
                self.driver.close()
                
                new_tab = self.driver.window_handles[0]
                self.driver.switch_to.window(new_tab)
                new_tab = self.driver.window_handles[-1]
                self.driver.switch_to.window(new_tab)
                self.driver.close()
                self.driver.switch_to.window(original_tab)
                self.driver.get("https://acme-test.uipath.com/home")  
                time.sleep(2)
                return "update realizado com sucesso!"
            else:

                print("Alert Text:", alert_text)
        except:
            print("Não foi possível realizar update, verificar...")
            self.driver.close()
            return "Caso desconhecido, não foi possível realizar update"
        
        

    def read_pdf(self, ID):
        
        
        all_files = os.listdir(self.pdf_dir)
        pdf_files = [file for file in all_files if file.endswith('.pdf')] 

        pdf_file_path = os.path.join(self.pdf_dir, pdf_files[0])

        pdfFileObj = open(pdf_file_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdfFileObj)        
        
        num_pages = len(pdf_reader.pages)
        pageObj = pdf_reader.pages[0]
        #extractedData = pageObj.extract_text()
        
        
        pa = pageObj.extract_text()
        pab = pa.splitlines()
        pdfFileObj.close()

        return pab, pdf_file_path


        


    def fetch_data(self):
                
        result_list = self.driver.find_elements(By.XPATH,"(//table[@class='table']//tr//td[text() = 'WI2'])")
        control = 1

        for n in range(len(result_list)):
            
            link = self.driver.find_element(By.XPATH,f"((//table[@class='table']//tr//td[text() = 'WI2']//preceding-sibling::td)/a)[{control}]")
            
            #Rotina para baixar o documento
            original_tab = self.driver.current_window_handle
            actions = ActionChains(self.driver)
            
            actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
            new_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_tab)
            
            pdf_link = self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary']//ancestor::a")
            pdf_link.click()
            time.sleep(3)

            #Manipulando e unindo dados do PDF
            ID = self.driver.find_elements(By.XPATH,"(//div[@class='col-lg-5']//child::p//b)")
        
            details_element = self.driver.find_element(By.XPATH, "((//div[@class='col-lg-5']//p)//following::p)[1]")
            details_string = details_element.text

            details_lines = details_string.split('\n')
            details_dict = {}

            for line in details_lines:
                
                key, value = line.split(': ')
                
                details_dict[key] = value
            
            print(details_dict)
            wiid_value = details_dict['WIID']
            print("WIID:", wiid_value)
            
            time.sleep(4)
            
            lista, arch_name = self.read_pdf(wiid_value)
            try:
                os.remove(arch_name)
                print(f"Documento {arch_name} removido com sucesso")
            except:
                print(f"Documento {arch_name} não encontrado, pode já ter sido deletado")        

            details_dict['Client_Name'] = lista[26]
            details_dict['Client_Request_ID'] = lista[27]
            details_dict['Client_Check_Number'] = lista[29]
            details_dict['Client_Check_Date'] = lista[30]
            

            self.data_man.save_csv(wiid_value, details_dict)

            self.driver.close()
            self.driver.switch_to.window(original_tab)
            
            control = control+2

        return print("Rolando página para próxima busca...")
        
        
    def loop_data(self):
        while True:
            
            self.fetch_data()
            try:
                if self.click_next() == "Não foi possível mais clicar na proxima página da lista ":
                    print("Busca de dados finalizada com sucesso!")
                    break
                
            except :
                print("Busca de dados interrompida, verificar")
                break
            
        

        


        


        #for i in range(len(result_list)):
            
            #cells = row.find_elements(By.XPATH,".//td")
            

        

        #df = pd.DataFrame(columns=['Actions', 'WIID', 'Description', 'Type', 'Status', 'Date'])

        


    
'''if __name__ == "__main__":    
    chrome_driver_manager = ChromeDriverManager()
    driver = chrome_driver_manager.get_driver()'''