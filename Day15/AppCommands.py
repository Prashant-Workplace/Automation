from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver: WebDriver=webdriver.Chrome()
driver.get("https:redbus.in")
driver.implicitly_wait(5)
driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# print(driver.find_element(By.ID,"mfGlobalSearchInput").is_displayed())
# print(driver.find_element(By.ID,"mfGlobalSearchInput").is_enabled())
# driver.find_element(By.XPATH,"//*[@id='poll-6084-1']").click()
# print(driver.find_element(By.XPATH,"//*[@id='poll-6084-1']").is_selected())

driver.find_element(By.XPATH,"//*[@id='help_redcare']/div/span").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='help_redcare']/div/span").click()
time.sleep(5)
driver.close()
# driver.quit()