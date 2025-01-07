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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.maximize_window()

driver.switch_to.frame("iframeResult")
obj=driver.find_element(By.XPATH,"/html/body/button")
act=ActionChains(driver)
act.double_click(obj).perform()
