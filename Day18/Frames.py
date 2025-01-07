import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//h5[normalize-space()='iFrame Demo']").click()
driver.switch_to.frame("//iframe[@src='MultipleFrames.html']")
time.sleep(5)
driver.close()

