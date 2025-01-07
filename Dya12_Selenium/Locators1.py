from logging import root
import app
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


# driver=webdriver.Chrome()
# driver.get("https://demo.nopcommerce.com/")
# time.sleep(5)
# driver.maximize_window()
# time.sleep(5)
# # #driver.find_element(By.ID,"Email").clear()
# # #driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# # #driver.find_element(By.NAME,"Password").send_keys("admin")
# # # driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()
# # driver.find_element(By.LINK_TEXT,"Register").click()
# # time.sleep(100)


# driver=webdriver.Chrome()
# driver.get("https://www.mi.com/in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Discover").click()
# driver.implicitly_wait(5)
# driver.find_element(By.CSS_SELECTOR,"#root > div > main > div.recommend-page > div.discover-list.recommend-list > div.discover-list__container > div > div > div:nth-child(2) > div.item-playwithmi-cover").click()
# time.sleep(5)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(10)
# driver.find_element(By.LINK_TEXT,"Join Our Team").click()
# driver.implicitly_wait(5)
# driver.close()

driver=webdriver.Chrome()
driver.get("https://facebook.com")
driver.implicitly_wait(5)
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("xyz")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("xyz")
# driver.find_element(By.CSS_SELECTOR,'input[placeholder="Email address or phone number"]').send_keys("xyz")
# driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid="royal_pass"]').send_keys("xyz")
driver.find_element(By.XPATH,'//*[@href="/r.php?entry_point=login"]').click()
# time.sleep(5)
# driver.close()
# input("press enter to close browser")
