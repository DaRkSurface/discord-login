#####################################################
# Author: drk
# Date: Oct 16 2021
# Made for improving my skills in Python and Selenium
#####################################################

#Importing Modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#Some important variables
PATH = r"/home/drk/Desktop/selenium/chromedriver"
driver = webdriver.Chrome(PATH)
site = "https://discord.com/login"

#Credentials
email = "hello@bro.com"
passwd = "nah123"

driver.get(site)
print("\nEntered", driver.title)

emailelm = driver.find_element(By.NAME, "email")
emailelm.send_keys(email)

passwordelm = driver.find_element(By.NAME, "password")
passwordelm.send_keys(passwd)

passwordelm.submit()