from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import the Service class

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver_path = r'D:\selenium_python\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)
query = 'Laptop'
driver.get(f"https://www.amazon.in/s?k={query}&crid=2GBCZSU9R85XX&sprefix=laptop%2Caps%2C259&ref=nb_sb_noss_2")


elem = driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.text)
print(elem.get_attribute("outerHTML"))

time.sleep(15)  
driver.close()