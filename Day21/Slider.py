import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

left=driver.find_element(By.XPATH,"//span[@style='left: 0%;']")
right=driver.find_element(By.XPATH,"//span[@style='left: 100%;']")

print(left.location,right.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(left,100,0).drag_and_drop_by_offset(right,-100,0).perform()

time.sleep(3)
driver.quit()
