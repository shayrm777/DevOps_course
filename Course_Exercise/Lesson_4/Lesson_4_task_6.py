"""
5.
    * Open Youtube web page
    * Type a name of a song
    * Click on search.
6.
    * Open Chrome browser on Google Translate website:
        https://translate.google.com/
        Find translation text field (the one you send keys to) with 3 different locators and print the WebElement
        you created.
7.
    * Open Chrome browser on Facebook website
        https://www.facebook.com/
        Login into Facebook (No need to send me credentials).
"""

import os
from selenium_setup import open_page
from selenium_setup import By
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui


url_page = "https://youtube.com"
song_name = "Peter Murphy - Strange Kind Of Love"

driver = open_page(url_page)
search_elm = driver.find_element("name", "search_query")
search_elm.send_keys(song_name)
search_elm.submit()
sleep(10)

# playing the song from the results
play_song = driver.find_element("xpath", f"//a[@title=\"{song_name}\"]").click()

# Find the "Skip Ad" button and press it
wait = ui.WebDriverWait(driver, 300)

skip_not_found = True
while skip_not_found:
    try:
        if EC.presence_of_element_located((By.XPATH,".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")):
            button=driver.find_element("xpath", ".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
            driver.execute_script("arguments[0].click();", button)
            print("Skipped")
            sleep(2)
            skip_not_found = False
            continue
        else:
             continue
    except NoSuchElementException:
        print("skip button not found")
        sleep(2)

print("Skip found and skipped...playing video for 30 seconds")
sleep(30)
driver.quit()
print(f"Loading page: {song_name} Done")


