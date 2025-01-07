from selenium import webdriver
from selenium.webdriver.common.by import By
from Day24 import ExcelUtility

filename=r"C:\Users\Prashant\Downloads\Toyota.xlsx"
sheetname="Data1"

option=webdriver.ChromeOptions()
option.add_argument("--headless")
driver=webdriver.Chrome(options=option)
driver.get("https://fd-calculator.in")
driver.maximize_window()
driver.find_element(By.ID,"amountInputField").send_keys("10000")
driver.find_element(By.ID,"periodInputField").send_keys("5")
driver.find_element(By.ID,"interestInputField").send_keys("10")
driver.find_element(By.ID,"calculateButton").click()
if driver.find_element(By.ID,"futureValue").text=="0.2 Lakh":
    ExcelUtility.writedata(filename,sheetname,2,6,"Pass")
else:
    ExcelUtility.writedata(filename,sheetname,2,6,"Fail")

driver.find_element(By.ID,"amountInputField").clear()
driver.find_element(By.ID,"amountInputField").send_keys("20000")
driver.find_element(By.ID,"calculateButton").click()
if driver.find_element(By.ID,"futureValue").text=="0.3 Lakh":
    ExcelUtility.writedata(filename, sheetname, 3, 6, "Pass")
else:
    ExcelUtility.writedata(filename, sheetname, 3, 6, "Fail")

driver.find_element(By.ID,"amountInputField").clear()
driver.find_element(By.ID,"amountInputField").send_keys("30000")
driver.find_element(By.ID,"calculateButton").click()
if driver.find_element(By.ID,"futureValue").text=="0.5 Lakh":
    ExcelUtility.writedata(filename, sheetname, 4, 6, "Pass")
else:
    ExcelUtility.writedata(filename, sheetname, 4, 6, "Fail")

driver.find_element(By.ID,"amountInputField").clear()
driver.find_element(By.ID,"amountInputField").send_keys("40000")
driver.find_element(By.ID,"calculateButton").click()
if driver.find_element(By.ID,"futureValue").text=="0.7 Lakh":
    ExcelUtility.writedata(filename, sheetname, 5, 6, "Pass")
else:
    ExcelUtility.writedata(filename, sheetname, 5, 6, "Fail")

driver.find_element(By.ID,"amountInputField").clear()
driver.find_element(By.ID,"amountInputField").send_keys("50000")
driver.find_element(By.ID,"calculateButton").click()
if driver.find_element(By.ID,"futureValue").text=="0.8 Lakh":
    ExcelUtility.writedata(filename, sheetname, 6, 6, "Pass")
else:
    ExcelUtility.writedata(filename, sheetname, 6, 6, "Fail")

driver.quit()

