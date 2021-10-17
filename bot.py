#####################################################
# Author: drk
# Date: Oct 16 2021
# Made for improving my skills in Python and Selenium
# DISCONTINUED...
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
#Download chrome driver at https://chromedriver.chromium.org/downloads (Check your browser version.
PATH = r"Path/to/chromedriver"
driver = webdriver.Chrome(PATH)
site = "discord url to server/channel or whatever"

#Credentials
email = "email to account"
passwd = "password to account"

driver.get(site)
print("\nEntered", driver.title)

emailelm = driver.find_element(By.NAME, "email")
emailelm.send_keys(email)

passwordelm = driver.find_element(By.NAME, "password")
passwordelm.send_keys(passwd)

passwordelm.submit()
