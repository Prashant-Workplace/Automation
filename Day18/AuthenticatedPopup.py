import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

