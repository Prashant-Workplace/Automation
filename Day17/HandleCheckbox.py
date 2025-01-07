import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
# driver.find_element(By.ID,"sunday").click()

select=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# print(len(select))
# for i in range(len(select)):
#     select[i].click()
# for i in select:
#     i.click()
# for i in select:
#     weekname=i.get_attribute("id")
#     if weekname=="sunday" or weekname=="monday":
#         i.click()

# for i in range(len(select)):
#     if i<5:
#         select[i].click()

for i in range(len(select)):
    select[i].click()
time.sleep(5)
for i in range(len(select)):
    select[i].click()
# driver.quit()

