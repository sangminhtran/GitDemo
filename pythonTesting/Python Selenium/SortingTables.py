import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

BrowserSortedveggieList = []

# click column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all rau củ name -> BrowserSortedveggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    BrowserSortedveggieList.append(ele.text)

originalBrowserSortedList = BrowserSortedveggieList.copy()  # copy List

# sort BrowserSortedveggieList -> newSortedList
BrowserSortedveggieList.sort()  # List này tự sort giá trị chính nó, ko phải tạo list mới

assert BrowserSortedveggieList == originalBrowserSortedList

