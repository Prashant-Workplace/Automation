from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.etmoney.com/stocks/market-data/all-time-low/10")
driver.implicitly_wait(5)
driver.maximize_window()
driver.implicitly_wait(5)
# # textmsg=driver.find_element(By.XPATH, "//a[contains(text(), 'Suraksha Diagnostic Ltd.')]/self::a").text
# # print(textmsg)
# # textmsg=driver.find_element(By.XPATH, "//a[contains(text(), 'Suraksha Diagnostic Ltd.')]/parent::div").text
# child=driver.find_elements(By.XPATH, "//a[contains(text(), 'Suraksha Diagnostic Ltd.')]/ancestor::tbody/child::tr")
# child=driver.find_elements(By.XPATH, "//a[contains(text(), 'Suraksha Diagnostic Ltd.')]/ancestor::tr/descendant::*")

child=driver.find_elements(By.XPATH, "//a[contains(text(), 'Suraksha Diagnostic Ltd.')]/ancestor::body/following::*")
print(len(child))
time.sleep(2)









