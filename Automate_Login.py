# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:36:53 2024

@author: gangylee

@info:
        > https://www.selenium.dev/documentation/webdriver/
        > https://www.selenium.dev/documentation/
        > Check for your Chrome browser version : https://www.whatismybrowser.com/
        > Download ChromeDriver : https://developer.chrome.com/docs/chromedriver/downloads/version-selection

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

webpage = "http://automated.pythonanywhere.com/login/"
service = Service('C:\\Users\\gangylee\\.spyder-py3\\gylee_scripts\\chromedriver.exe')

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get(webpage)
  return driver

def main(run=False):
  driver = get_drvier()

  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  print(driver.current_url)
  
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)
    
main()