from deskapp import DeskAPP
from webapp import ChromeDriverManager
from data import DataManager
import time



chrome_driver_manager = ChromeDriverManager()
data_man = DataManager()

#driver = chrome_driver_manager.get_driver()

#chrome_driver_manager.fetch_data()

#
#chrome_driver_manager.update_status(1)

#Login
chrome_driver_manager.login()
#Baixa arquivos e organiza dados
chrome_driver_manager.loop_data()


count = data_man.files_list_csv_count()

for n in range(len(count)):
    print("testando")
    chrome_driver_manager.search_check(n)
    chrome_driver_manager.submit_check(n)
    chrome_driver_manager.update_status(n)
    


#desk_app = DeskAPP()
#desk_app.login()

#time.sleep(12)
#desk_app.search_client()




#chrome_driver_manager.search()
#time.sleep(2)
#driver.quit()
