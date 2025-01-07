import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable -notifications")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("Number of rows in table :", len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")))
print("Number of columns in table :", len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")))
# tabletext=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(tabletext)
# for r in range(2, 7):
#     for c in range(1, 5):
#         data = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{c}]")
#         print(data.text,end=" ")
#     print()

for r in range (2,7):
    data = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{2}]")
    if data.text=="Mukesh":
            book=driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{1}]")
            price = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{4}]")
            print(data.text, book.text, price.text)

