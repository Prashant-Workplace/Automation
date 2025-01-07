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

driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()

obj=driver.find_element(By.ID,"myLink1")
act=ActionChains(driver)
act.context_click(obj).perform()