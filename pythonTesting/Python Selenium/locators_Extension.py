import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/client/auth/login')

driver.find_element(By.LINK_TEXT, 'Forgot password?').click()  # element là cái link click - tag a

# xác định element từ parent đến child CSS
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys('demo@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys('Hello@1234')
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('Hello@1234')
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click() # xđ element với text