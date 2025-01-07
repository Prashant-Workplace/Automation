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

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()
time.sleep(3)

driver.execute_script("window.scrollBy(0,3000)","")
pixle=driver.execute_script("return window.pageYOffset;")
print(pixle)
time.sleep(3)

india=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/div/div/div[79]/div/a/img")
driver.execute_script("arguments[0].scrollIntoView();",india)
pixle=driver.execute_script("return window.pageYOffset;")
print(pixle)
time.sleep(3)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(3)
driver.quit()



