import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()                   # verify đã check chưa
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()  # check điều kiện false

time.sleep(3)