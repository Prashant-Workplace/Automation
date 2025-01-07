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

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
act=ActionChains(driver)

obj1=driver.find_element(By.ID,"box3")
obj2=driver.find_element(By.ID,"box103")

act.drag_and_drop(obj1,obj2).perform()
