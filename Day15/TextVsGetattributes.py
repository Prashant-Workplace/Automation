from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
time.sleep(3)
driver.maximize_window()
x=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
x.send_keys("laptop")
print("result:",x.get_attribute("value"))