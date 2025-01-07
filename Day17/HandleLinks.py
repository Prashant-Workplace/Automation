import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Hidden Elements & AJAX").click()
# driver.find_element(By.LINK_TEXT,"Home").click()
# links=driver.find_elements(By.TAG_NAME,"a")
links=driver.find_elements(By.XPATH,"//a")
print(len(links))
for i in links:
    print(i.text)