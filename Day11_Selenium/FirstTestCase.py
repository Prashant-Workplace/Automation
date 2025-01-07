import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

service = Service(executable_path="C:/Driver/chromedriver/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=service)

driver.get("https://admin-demo.nopcommerce.com/")
# driver.find_element(By.ID,"APjFqb").send_keys("nseindia")
# #driver.find_element(By.ID,"APjFqb").send_keys(Keys.ENTER)
# time.sleep(5)
# driver.find_element(By.ID,"CcAdNb").click()
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
time.sleep(20)
