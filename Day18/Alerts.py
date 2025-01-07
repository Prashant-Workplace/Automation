import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# alert=driver.switch_to.alert
# print(alert.text)
# alert.send_keys("welcome")
# # alert.accept()
# alert.dismiss()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.find_element(By.NAME,"proceed").click()
time.sleep(5)
alert=driver.switch_to.alert
print(alert.text)
time.sleep(5)
alert.accept()
