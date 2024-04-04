import os
import pandas as pd
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import csv

class DataManager:
    def __init__(self):
        
        #self.driver = webdriver.Chrome()
        load_dotenv()
        self.csv_dir = os.getenv("DATA_PATH")
        self.pdf_dir = os.getenv("PDF_PATH")
        self.save_directory = self.csv_dir

    def set_save_directory(self, directory):
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.save_directory = directory

    def save_csv(self, filename, data_dict):
               
        for key, value in data_dict.items():
            print(f"Key: {key}, Value: {value}")
            
        
        df = pd.DataFrame.from_dict(data_dict, orient='index').T
        csv_file_path = os.path.join(self.csv_dir, filename+".csv")
        
        #Abaixo salva como text
        #csv_file_path = os.path.join(self.csv_dir, filename+".csv")

        df.to_csv(csv_file_path, index=False)
        

        '''with open('testando.csv', 'a') as f:
            new_df.to_csv(f, header=False, index=False)'''

    
        '''if self.save_directory is None:
            raise ValueError("Save directory is not set. Call set_save_directory() first.")

        file_path = os.path.join(self.save_directory, filename)'''

