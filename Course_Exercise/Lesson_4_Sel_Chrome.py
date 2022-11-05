"""
Class 4
Write a program that does the following:
1. Write a script which will open the following:
    a. Chrome – http://www.walla.co.il
    b. FireFox – http://www.ynet.co.il

2. In one of the browsers you open do the following:
    a. Create a variable with the website’s title
    b. Refresh website
    c. Get website name and compare it to the variable you created in clause 1.

3. Open a few browsers, locate any element, does the element has the same locators in the other browser?

4. Create a test with the following:
    * Open Google Translate web page
    * Write anything in Hebrew in the text area
"""

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#from webdriver_manager.chrome import ChromeDriverManager

#options.add_argument("start-maximized")

def get_page_title(driver):
    title = driver.title
    return title

chrome_driver = os.path.join(os.getcwd(), "chromedriver_win32", "chromedriver.exe")
chrome_services = Service(chrome_driver)
chrome_options = Options()

url_ynet = "http://www.ynet.co.il"
url_google = "https://www.google.com"
driver_chrome = webdriver.Chrome(service=chrome_services, options=chrome_options)

driver_chrome.maximize_window()

driver_chrome.get(url_ynet)

page_title = get_page_title(driver_chrome)
print(f"Before page refresh page title is: {page_title}")

# refresh page
sleep(10)
driver_chrome.refresh()
print(f"Page Name: {driver_chrome.current_url}")

driver_chrome.quit()

#driver_chrome.quit()

