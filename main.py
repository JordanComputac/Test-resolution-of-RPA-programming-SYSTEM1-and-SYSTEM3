from deskapp import DeskAPP
from webapp import ChromeDriverManager
from data import DataManager
import time



chrome_driver_manager = ChromeDriverManager()
#driver = chrome_driver_manager.get_driver()
chrome_driver_manager.login()
chrome_driver_manager.fetch_data()


data_man = DataManager()


desk_app = DeskAPP()
desk_app.login()




#chrome_driver_manager.search()
time.sleep(2)
#driver.quit()
