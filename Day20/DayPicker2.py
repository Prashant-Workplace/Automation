import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.ID, "dob").click()
month = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_value("11")
month = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
month.select_by_value("2000")
date = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for i in date:
    if i.text == "20":
        i.click()
        break
time.sleep(3)
driver.close()
