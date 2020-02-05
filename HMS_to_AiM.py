__author__ = "Tim Zong"
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import getpass

class AiM():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.driver.get("https://www.aimdemo.ualberta.ca/fmax/login")
        self.driver.set_window_size(1900, 1020)
        username = input('Enter your username (AiM): ')
        password = getpass.getpass('Enter your password (AiM): ')
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login").click()

    def customer_request(self,description,reference,property="51000"):
        return None

class ResCenter():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.driver.get("https://reztest.ancillary.ualberta.ca/ResCenter/")
        self.driver.maximize_window()
        # self.driver.set_window_size(1900, 1020)
        username = input('Enter your username (ResCenter): ')
        password = getpass.getpass('Enter your password (ResCenter): ')
        self.driver.find_element(By.ID, "ctl00_mainContent_txtUserName_cbTextBox").send_keys(username)
        self.driver.find_element(By.ID, "ctl00_mainContent_txtPassword_cbTextBox").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_btnLogin_CBORDLinkButton > .btn-text").click()

    def search(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".fa-bars").click()

        self.driver.find_element(By.ID, "FacilitiesModule").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Maintenance")))
        self.driver.find_element(By.LINK_TEXT, "Maintenance").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Work Orders")))
        self.driver.find_element(By.LINK_TEXT, "Work Orders").click()
        self.driver.find_element(By.ID, "ctl00_mainContent_ddWOStatus").click()
        dropdown = self.driver.find_element(By.ID, "ctl00_mainContent_ddWOStatus")
        dropdown.find_element(By.XPATH, "//option[. = 'NEW']").click()
        self.driver.find_element(By.ID, "ctl00_mainContent_ddWOStatus").click()
        self.driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_btnRunSearch_CBORDLinkButton > .btn-text").click()

    def top_record(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_mainContent_radgridWorkOrders_ctl00_ctl04_btnSelect_CBORDLinkButton")))
        self.driver.find_element(By.ID, "ctl00_mainContent_radgridWorkOrders_ctl00_ctl04_btnSelect_CBORDLinkButton").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_mainContent_txtDescription_ReadOnlyBox pre")))
        description_res = self.driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_txtDescription_ReadOnlyBox pre").text
        WO_res = self.driver.find_element(By.ID, "ctl00_mainContent_txtWOIDNum_cbTextBox").get_attribute("value")
        location_res = self.driver.find_element(By.ID, "ctl00_mainContent_FacilityLookup_txtFacilityNameSearch").get_attribute("value")
        return (WO_res,description_res,location_res)

if __name__ == '__main__':
    # aim_window = AiM()
    res_window = ResCenter()

    # aim_window.setup_method()
    res_window.setup_method()

    # aim_window.login()
    res_window.login()
    res_window.search()
    res_Wo,res_des,res_loc = res_window.top_record()

    time.sleep(10)