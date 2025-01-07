import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(3)
windowIDs=driver.window_handles
# driver.switch_to.window(windowIDs[1])
for i in windowIDs:
    driver.switch_to.window(i)
    print(driver.title)
    if driver.title=="OrangeHRM":
        driver.close()






