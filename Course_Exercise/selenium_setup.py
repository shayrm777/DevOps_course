
"""
Generic Selenium setup
"""

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

def _chrom_setup():
    " Setting up chrome drivers, Options and services"
    chrome_driver = os.path.join(os.getcwd(), "chromedriver_win32", "chromedriver.exe")
    chrome_services = Service(chrome_driver)
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=chrome_services, options=chrome_options)
    return driver

def open_page(url):
    driver = _chrom_setup()
    driver.get(url)
    return driver
