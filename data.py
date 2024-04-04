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


    def files_list_csv_count(self):
        csv_dir = self.csv_dir    
        all_files = os.listdir(csv_dir)

        csv_files = [file for file in all_files if file.endswith('.csv')]
        csv_file_names = list(map(lambda x: x, csv_files))

        return csv_file_names

    def files_list_csv(self, iterat):
        csv_dir = self.csv_dir    
        all_files = os.listdir(csv_dir)

        csv_files = [file for file in all_files if file.endswith('.csv')]
        csv_file_names = list(map(lambda x: x, csv_files))

        return csv_file_names[iterat]


    def get_check_number(self, file):
        
        path_csv = self.csv_dir+f"\\{file}"
        df = pd.read_csv(path_csv)

        value = df.loc[0, "Client_Check_Number"]

        return value

    def get_date(self, file):
        
        path_csv = self.csv_dir+f"\\{file}"
        df = pd.read_csv(path_csv)
                
        value = df.loc[0, "Date"]

        return value

    def get_date_detail(self, date_string):
        
        year, month, day = date_string.split("-")

        month_name = {
            "01": "January", "02": "February", "03": "March", "04": "April",
            "05": "May", "06": "June", "07": "July", "08": "August",
            "09": "September", "10": "October", "11": "November", "12": "December"
        }[month]

        

        return year, month_name, day
    
    def get_client_request_id(self, file):

        path_csv = self.csv_dir+f"\\{file}"
        df = pd.read_csv(path_csv)
                
        value = df.loc[0, "Client_Request_ID"]

        return value





'''data_man = DataManager()

file = data_man.files_list_csv(0)
value = data_man.get_client_request_id(file)
print(value)
year, month_name, day = data_man.get_date_detail(value)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)'''


