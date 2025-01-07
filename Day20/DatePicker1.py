import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

month="January"
year="2024"
date="1"

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.ID,'datepicker').click()

while True:
    mon = driver.find_element(By.XPATH, "//*[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//*[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//*[@class='ui-icon ui-icon-circle-triangle-w']").click()

day=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//*/a")

for d in day:
    if d.text==date:
        d.click()
        break
driver.quit()