"""
8.
    Open Chrome browser on any webpage.
    Delete all cookies from browser.
    Make sure all cookies are deleted by printing all cookies stored in the browser.
"""
import json
from time import sleep
from selenium_setup import open_page

url = "https://google.com"

def get_and_print_cookies(driver):
    cookies = driver.get_cookies()
    if cookies:
        print(f"got this values for cookies {cookies}")
        print(json.dumps(cookies[0], sort_keys=True, indent=4))
    else:
        print("No cookies here...")


driver = open_page(url)
driver.add_cookie({"name": "Shay", "value": "one two"})
get_and_print_cookies(driver)
sleep(3)

print(f"deleting all cookies from page: {url}")
driver.delete_all_cookies()
get_and_print_cookies(driver)

sleep(3)
driver.quit()
