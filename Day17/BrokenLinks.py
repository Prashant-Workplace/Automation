import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown#google_vignette")
driver.implicitly_wait(10)
driver.maximize_window()
dropdown=Select(driver.find_element(By.ID,"country"))
dropdown.select_by_visible_text("India")