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
    filename = str(random.randint(10000000,99999999)) + ".jpg"
    fp = open(SAVE_PATH + filename, 'wb')
    fp.write(r.content)
    fp.close()
    print("saved image" + filename)

IG_LINK = 'https://www.instagram.com/alderight'
USERNAME = 'alderight'
PASSWORD = 'Awesomesince(1997)1'
SAVE_PATH = os.path.abspath(os.getcwd()) + "\\downloads\\" + USERNAME + "\\"

try:
    os.makedirs(SAVE_PATH)
except:
    print("SAVE PATH already exists. Proceeding...")

driver = webdriver.Chrome(r"C:\Users\Arceus\Desktop\Web Scraping Practice\chromedriver_win32\chromedriver.exe")

driver.get(r'' + IG_LINK)

time.sleep(5)
driver.find_element("name","username").send_keys(USERNAME)
time.sleep(0.5)
driver.find_element("name","password").send_keys(PASSWORD)
time.sleep(0.7)
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(5)

driver.get(r'' + IG_LINK)
time.sleep(5)

# traverse page length
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# save all cover photos
sources = []
elements = driver.find_elements(By.XPATH,"//img[@class='_aagt']")
for e in elements:
    src = e.get_attribute("src")
    sources.append(src)
    save_image(src)

# deep traverse photos
clickables = driver.find_elements(By.XPATH,"//*/article//div//div//div//div//a")
for c in clickables:
    c.click()
    page = 0
    # repeat 9 more times or up to limit
    while page < 9:
        time.sleep(1)
        try:
            # click next button
            driver.find_element(By.XPATH, "//button[@aria-label='Next']").click()
            # check if already saved
            elements = driver.find_elements(By.XPATH,"//img[@class='_aagt']")
            for e in elements:
                src = e.get_attribute("src")
                if not src in sources:
                    sources.append(src)
                    save_image(src)
        except:
            print('No more next buttons')
            break
        page = page + 1
    driver.execute_script("window.history.go(-1)")

exit()