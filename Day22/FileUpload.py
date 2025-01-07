import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='input-4']").send_keys(r"C:\Users\Prashant\Desktop\Aptitude-Questions-and-Answers-PDF.pdf")

time.sleep(3)
driver.quit()