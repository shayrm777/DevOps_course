"""
Lesson 4 - Selenium
3. Open a few browsers, locate any element, does the element has the same locators in the other browser?

"""

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_page_title(driver):
    title = driver.title
    return title

chrome_driver = os.path.join(os.getcwd(), "../chromedriver_win32", "chromedriver.exe")
chrome_services = Service(chrome_driver)
chrome_options = Options()
chrome_options.add_argument("start-maximized")

#url_ynet = "http://www.ynet.co.il"
#url_google = "https://www.google.com"
#url_github = "https://github.com"
url_one = "https://www.one.co.il/"

driver_chrome = webdriver.Chrome(service=chrome_services, options=chrome_options)

#driver_chrome.maximize_window()

driver_chrome.get(url_one)
print("Loading page: Done")

element_1 = driver_chrome.find_element("id", "one-search").send_keys("messi")
element_2 = driver_chrome.find_element("id", "aAccessibility")
driver_chrome.execute_script("javascript:DoSearch($j('#one-search').val());", element_2)

print(element_2)
