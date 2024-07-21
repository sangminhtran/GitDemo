import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# locators: ID, Xpath, CSS Selector, Classname, name, linkText
driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()

# syntax Xpath: //tagname[@attribute='value'] => //input[@type='submit']
# syntax CSS Selector: tagname[attribute='value'] => input[type='submit'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name'").send_keys('Sang')
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

# Static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

assert 'Success' in message  # verify

# sử dụng Xpath chỉ định element ở vị trí [n]
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('helloagain')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()  # remove text



time.sleep(3)