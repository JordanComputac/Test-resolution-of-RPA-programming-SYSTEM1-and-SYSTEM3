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
            return print("Procurando por mais categorias WI2...")
        except:
            print("Não foi possível mais clicar na proxima página da lista ")
            return None
            
        
    def search_cchek(self):
            self.driver.get("https://acme-test.uipath.com/home")


            
    def read_pdf(self, ID):
        
        
        all_files = os.listdir(self.pdf_dir)
        pdf_files = [file for file in all_files if file.endswith('.pdf')] 

        pdf_file_path = os.path.join(self.pdf_dir, pdf_files[0])

        pdfFileObj = open(pdf_file_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdfFileObj)

        
        
        num_pages = len(pdf_reader.pages)
        pageObj = pdf_reader.pages[0]
        extractedData = pageObj.extract_text()
        
        sections = extractedData.strip().split('\n\n')
        lista = []

        for section in sections:
            print(section.strip())
            breakpoint()
            lista.append(section.strip())

        '''lista = []
        _ = list(map(lambda x: lista.append(x.strip()), sections))        
       '''
        return lista, pdf_file_path


        


    def fetch_data(self):
        
        #result_list = self.driver.find_elements(By.XPATH,"//table[@class='table']//child::tr")
        result_list = self.driver.find_elements(By.XPATH,"(//table[@class='table']//tr//td[text() = 'WI2'])")

        link = self.driver.find_element(By.XPATH,"((//table[@class='table']//tr//td[text() = 'WI2']//preceding-sibling::td)[1]/a)[1]")
        #link = link.get_attribute("href")
        original_tab = self.driver.current_window_handle
        actions = ActionChains(self.driver)
        
        actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        
        pdf_link = self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary']//ancestor::a")
        pdf_link.click()
        
        
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
        
        breakpoint()
        #os.remove(arch_name)  
        self.data_man.save_csv("testando", details_dict)

        

        self.driver.close()
        self.driver.switch_to.window(original_tab)
        self.click_next()


        


        #for i in range(len(result_list)):
            
            #cells = row.find_elements(By.XPATH,".//td")
            

        

        #df = pd.DataFrame(columns=['Actions', 'WIID', 'Description', 'Type', 'Status', 'Date'])

        


    
'''if __name__ == "__main__":    
    chrome_driver_manager = ChromeDriverManager()
    driver = chrome_driver_manager.get_driver()'''