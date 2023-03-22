from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver_path = r"C:\Users\vicferre\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\Dev\chromedriver\chromedriver"
#^^above must be the driver's path in your computer
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org")
print (driver.title)
time.sleep(10)
print('Terminou')
