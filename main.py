# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # driver = webdriver.Chrome()
# # options = webdriver.ChromeOptions()
# # options.add_experimental_option("useAutomationExtension", False)
# # options.add_experimental_option("excludeSwitches",["enable-automation"])

# # driver_path = r'/chromedriver.exe'
# # driver = webdriver.Chrome(executable_path = driver_path, options = options)

# # driver.get("http://www.python.org")
# # assert "Python" in driver.title
# # elem = driver.find_element(By.NAME, "q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# # time.sleep(6)
# # driver.close()
# from selenium.webdriver.chrome.options import Options
# import selenium
# chrome_options = Options()
# chrome_options.add_argument("--disable-gpu")

# driver = webdriver.Chrome(options=chrome_options)
# driver.switch_to.window(driver.window_handles[0])
# try:
#     driver.get('https://www.google.com/')
    
# except selenium.common.exceptions.NoSuchWindowException:
#     print("Browser window was closed. Re-initializing...")
#     driver = webdriver.Chrome()  # Ensure you initialize again if needed
#     driver.get('https://www.google.com/')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import the Service class
import time

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Path to your chromedriver.exe
driver_path = r'D:\selenium_python\chromedriver.exe'

# Use the Service class to specify the path to chromedriver
service = Service(executable_path=driver_path)

# Initialize the driver with Service and options
driver = webdriver.Chrome(service=service, options=options)

try:
    # Visit the website
    driver.get("http://www.python.org")

    # Check if "Python" is in the title
    assert "Python" in driver.title

    # Find the search box, clear it, and search for 'pycon'
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    # Verify the results
    assert "No results found." not in driver.page_source

    # Sleep for demonstration purposes
    time.sleep(6)

finally:
    # Ensure the browser is closed even if an error occurs
    driver.quit()
