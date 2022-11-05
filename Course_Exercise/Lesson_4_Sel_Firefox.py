import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
firefox_driver = os.path.join(os.getcwd(), "geckodriver-v0.30.0-win64", "geckodriver.exe")
firefox_services = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', user_agent)

# lunch Firefox browser
browser = webdriver.Firefox(service=firefox_services, options=firefox_options)
browser.get("https://ynet.co.il")