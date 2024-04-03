from deskapp import DeskAPP
from webapp import ChromeDriverManager
import time



chrome_driver_manager = ChromeDriverManager()
driver = chrome_driver_manager.get_driver()





driver.get("https://www.google.com")



desk_app = DeskAPP()
desk_app.close()

chrome_driver_manager.search()
time.sleep(2)
driver.quit()