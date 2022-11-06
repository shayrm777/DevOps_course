
from time import sleep
from selenium_setup import open_page

fb_url = "https://www.facebook.com/"
driver = open_page(fb_url)
login_email = driver.find_element("id", "email")
login_email.send_keys("fake_user@gmail.com")

login_password = driver.find_element("id", "pass")
login_password.send_keys("fake_password")
sleep(5)
login_password.submit()
sleep(15)
driver.quit()

