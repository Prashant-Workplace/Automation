import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get("https://jmeter.apache.org/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Download Releases").click()
driver.find_element(By.LINK_TEXT,"apache-jmeter-5.6.3.zip").click()

time.sleep(3)
driver.quit()







