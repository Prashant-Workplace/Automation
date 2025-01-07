import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/dropdown#google_vignette")
driver.maximize_window()
# dropdown=Select(driver.find_element(By.ID,"country"))
# dropdown.select_by_visible_text("India")
# time.sleep(2)
# dropdown.select_by_index(4)
# time.sleep(2)
# dropdown.select_by_value("AF")
# allopt=dropdown.options
# print(len(allopt))
#
# for i in allopt:
#     print(i.text)
#     if i.text=="India":
#         i.click()

allopt=driver.find_elements(By.XPATH,"//*[@id='country']/option")
print(len(allopt))



