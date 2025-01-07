import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
option.add_argument("--disable -notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.get("https://whatmylocation.com/")
driver.maximize_window()









