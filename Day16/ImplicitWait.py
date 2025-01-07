from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://google.com")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Selenium")
driver.find_element(By.NAME,"q").submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium Tutorial']").click()