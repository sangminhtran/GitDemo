import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

name = 'Sang'
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()

alert = driver.switch_to.alert  # switch sang alert (ko thể inspect vì alert java/js ko phải html)
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()  # accept() = OK, dismiss() = Cancel