"""
Lesson 4 - Selenium
--------------------------
4. Create a test with the following:
    * Open Google Translate web page
    * Write anything in Hebrew in the text area

"""

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_driver = os.path.join(os.getcwd(), "../chromedriver_win32", "chromedriver.exe")
chrome_services = Service(chrome_driver)
chrome_options = Options()
chrome_options.add_argument("start-maximized")


translate_url = "https://translate.google.com/??sl=iw&tl=en&text=" + "שלום" + "&op=translate"
print(translate_url)
#url = "https://translate.google.com/"

driver_chrome = webdriver.Chrome(service=chrome_services, options=chrome_options)

#driver_chrome.maximize_window()

driver_chrome.get(translate_url)
print("Loading page: Done")
