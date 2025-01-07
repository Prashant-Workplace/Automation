from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
time.sleep(3)
driver.maximize_window()
# links=driver.find_element(By.XPATH,"//div[@class='footer-upper']//a")
# print(links.text)
# links=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
# print(len(links))
# for x in links:
#     print(x.text)
# object=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(object))
# object[0].send_keys("laptop")
# time.sleep(2)
driver.find_elements(By.XPATH,"//input[@id='small-searchterms1']")
driver.quit()

