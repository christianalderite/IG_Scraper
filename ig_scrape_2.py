from pydoc import source_synopsis
from selenium import webdriver
import pandas as pd
from datetime import datetime
import logging
import time
import requests
import random
import os
from selenium.webdriver.common.by import By

def save_image(source):
    r = requests.get(source)
    filename = str(datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]) + ".jpg"
    fp = open(SAVE_PATH + filename, 'wb')
    fp.write(r.content)
    fp.close()
    print("saved image" + filename)

# CHANGE these based on your use case
IG_LINK = 'https://www.instagram.com/target_account'
USERNAME = 'YOURUSERNAME'
PASSWORD = 'YOURPASSWORD'

# CHANGE to your WebDriver location
WEB_DRIVER_PATH = r"C:\Users\Arceus\Desktop\Scraper\chromedriver_win32\chromedriver.exe"

# Rather not change this
SAVE_PATH = os.path.abspath(os.getcwd()) + "\\downloads\\" + IG_LINK.split("/")[-1] + "_" + str(time.strftime("%Y%m%d%H%M")) + "\\"

try:
    os.makedirs(SAVE_PATH)
except:
    print("SAVE PATH already exists. Proceeding...")

driver = webdriver.Chrome(WEB_DRIVER_PATH)

driver.get(r'' + 'https://www.instagram.com')

time.sleep(5)
driver.find_element("name","username").send_keys(USERNAME)
time.sleep(0.4)
driver.find_element("name","password").send_keys(PASSWORD)
time.sleep(0.7)
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(5)

driver.get(r'' + IG_LINK)
time.sleep(5)

sources = []

# open first photo set
driver.find_element(By.XPATH,"//*/article//div//div//div//div//a").click()

# traverse all photo sets
while True:
    page = 0
    # traverse each page of set
    while page < 9:
        time.sleep(1 + 0.01 * random.randint(10,50))
        try:
            # check if already saved
            elements = driver.find_elements(By.XPATH,"//img[@class='_aagt']")
            for e in elements:
                src = e.get_attribute("src")
                # save photo if not already saved
                if not src in sources:
                    sources.append(src)
                    save_image(src)
            # click next button to go to next page of set
            driver.find_element(By.XPATH, "//button[@aria-label='Next']").click()
        except:
            break
        page = page + 1
    
    try:
        # click next button to go to next set
        print('Loading next set...')
        input_el = driver.find_element(By.XPATH, "//*[local-name() = 'svg' and @aria-label='Next']")
        to_click = input_el.find_element(By.XPATH,"./../..")
        driver.execute_script("arguments[0].click();", to_click)
    except:
        print("No more sets. Finished.")
        break

#driver.close()
exit()