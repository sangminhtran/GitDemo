import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)

# chọn option từ dynamic dropdown
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")  # List items
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

#print(driver.find_element(By.ID, 'autosuggest').text)  # dynamic text nên text = ''
print(driver.find_element(By.ID, 'autosuggest').get_attribute('value'))  # get value trong field

assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'



time.sleep(3)