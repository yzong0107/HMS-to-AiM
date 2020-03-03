# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_mainContent_ddWOStatus")))
# self.driver.find_element(By.ID, "ctl00_mainContent_ddWOStatus").click()
# dropdown = self.driver.find_element(By.ID, "ctl00_mainContent_ddWOStatus")
# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[. = 'Assigned']")))
# dropdown.find_element(By.XPATH, "//option[. = 'Assigned']").click()  # change status to "Assigned"
# self.driver.find_element(By.ID, "ctl00_mainContent_ddWOStatus").click()

# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_mainContent_ddWOType")))
# self.driver.find_element(By.ID, "ctl00_mainContent_ddWOType").click()
# dropdown = self.driver.find_element(By.ID, "ctl00_mainContent_ddWOType")
# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[. = 'General']")))
# dropdown.find_element(By.XPATH, "//option[. = 'General']").click() # change type to "General"
# self.driver.find_element(By.ID, "ctl00_mainContent_ddWOType").click()

# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_mainContent_ddWOPriority")))
# self.driver.find_element(By.ID, "ctl00_mainContent_ddWOPriority").click()
# dropdown = self.driver.find_element(By.ID, "ctl00_mainContent_ddWOPriority") # change priority to "Normal"
# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[. = 'Normal']")))
# dropdown.find_element(By.XPATH, "//option[. = 'Normal']").click()
# self.driver.find_element(By.ID, "ctl00_mainContent_ddWOPriority").click()
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.aimdemo.ualberta.ca/fmax/login")
print ("Hello world")

#
# import xlwt
# import openpyxl
# import time
# from datetime import datetime
#
# wb = openpyxl.load_workbook("Logs.xlsx")
# ws = wb.worksheets[0]
# id = ws.cell(row=ws.max_row,column=1).value
# print (id,type(id))
# new_data = [[1,"123456","78910","Processed",datetime.now(),""],
#             [2,"654321","01987","Error","","Error message Location is a mandatory field"]]
#
# for row in new_data:
#     ws.append(row)
#
# wb.save("Logs.xlsx")


