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
file = 0
for i in range(1,21): 
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2GBCZSU9R85XX&qid=1732389836&sprefix=laptop%2Caps%2C259&ref=sr_pg_3")


    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print(f"{len(elems)} items found")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data1/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file+=1
        # print(elem.text) 
        # print(elem.text)

    # time.sleep(15)  
driver.close()