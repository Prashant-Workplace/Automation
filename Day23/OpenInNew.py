import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select
import os

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get("https://jmeter.apache.org/")
driver.maximize_window()
# driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')
driver.get("https://nseindia.com")
time.sleep(3)

# driver.find_element(By.LINK_TEXT,"License").send_keys(Keys.CONTROL+Keys.ENTER)

driver.quit()
