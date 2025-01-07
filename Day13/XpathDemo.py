from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://flipkart.com")
driver.implicitly_wait(5)
driver.maximize_window()
# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input").send_keys("poco")
# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button").click()
# time.sleep(5)

# driver.find_element(By.XPATH,"//*[@name='q' and @id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input").send_keys("poco")
# driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button").click()
# time.sleep(3)

# driver.find_element(By.XPATH,"//input[contains(@name,'q')]").send_keys("poco")
# driver.find_element(By.XPATH,"//input[starts-with(@title, 'Search')]").send_keys("poco")
driver.find_element(By.XPATH,"//a[text()='Become a Seller']").click()
# driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button").click()
time.sleep(2)



