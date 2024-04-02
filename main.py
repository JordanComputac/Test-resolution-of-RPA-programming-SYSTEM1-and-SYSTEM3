import time
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from selenium import webdriver

app = Application().start(cmd_line=r'"C:\Users\maema\Downloads\ACME-System3-v0.1\ACME-System3-v0.1\ACME-System3.exe"')
time.sleep(2)
app.ACMESystem3.Exit.click()

