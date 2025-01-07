from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=NoSuchElementException)
# driver.implicitly_wait(10)
driver.get("https://google.com")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Selenium")
driver.find_element(By.NAME,"q").submit()
# driver.find_element(By.XPATH,"//h3[text()='Selenium Tutorial']").click()
ST=wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium Tutorial']")))
ST.click()
driver.quit()