import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("selenium")
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()
time.sleep(3)
result = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
for i in result:
    print(i.text)
    i.click()
print(len(result))
ids = driver.window_handles
for i in ids:
    driver.switch_to.window(i)
    if driver.title == "Selenium dioxide - Wikipedia" or driver.title == "Selenium in biology - Wikipedia":
        driver.close()
time.sleep(5)
driver.quit()
