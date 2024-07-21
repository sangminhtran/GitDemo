import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles  # get window name của các tab đang open, push vào List

driver.switch_to.window(windowsOpened[1])  # switch to window con ở vị trí index 1
print(driver.find_element(By.TAG_NAME, 'h3').text)

driver.switch_to.window(windowsOpened[0])  # switch to window cha ở vị trí index 0
assert "Opening a new window" == driver.find_element(By.TAG_NAME, 'h3').text

time.sleep(3)

