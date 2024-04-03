import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ChromeDriverManager:
    def __init__(self):
        load_dotenv()
        #Abaixo só é necessário caso chromedriver esteja em outro diretorio
        self.chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
        
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver
    

    def search(self):

        search_bar = self.driver.find_element(By.CLASS_NAME, "gLFyf")

        # Type something in the search bar
        search_bar.send_keys("Python programming")

        # Press Enter (or submit the form)
        search_bar.send_keys(Keys.TAB)


'''if __name__ == "__main__":    
    chrome_driver_manager = ChromeDriverManager()'''