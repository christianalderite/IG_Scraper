from selenium import webdriver
import pandas as pd
from datetime import datetime
import logging
import time
import requests
import random
import os

IG_LINK = 'https://www.instagram.com/alderight'
USERNAME = 'alderight'
PASSWORD = 'Awesomesince(1997)1'
SAVE_PATH = os.path.abspath(os.getcwd()) + "\\downloads\\" + USERNAME + "\\"

os.makedirs(SAVE_PATH)


driver = webdriver.Chrome(r"C:\Users\Arceus\Desktop\Web Scraping Practice\chromedriver_win32\chromedriver.exe")

driver.get(r'' + IG_LINK)

time.sleep(0.2)
driver.find_element("name","username").send_keys(USERNAME)
time.sleep(0.3)
driver.find_element("name","password").send_keys(PASSWORD)
time.sleep(0.2)
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(0.2)

driver.get(r'' + IG_LINK)

elements = driver.find_elements("xpath","//*/div//img")

for e in elements:
    img_src = e.get_attribute("src")
    r = requests.get(img_src)
    filename = str(random.randint(10000000,99999999)) + ".jpg"
    fp = open(SAVE_PATH + filename, 'wb')
    fp.write(r.content)
    fp.close()