from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver=webdriver.Chrome()
driver.get("https:redbus.in")
time.sleep(3)
driver.maximize_window()
driver.get("https:amazon.in")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()