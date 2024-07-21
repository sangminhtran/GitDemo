import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
action = ActionChains(driver)

action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()  # move đến và hover
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  # click phải
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()

# Here is new comment

print("Sang")
print("Nha")
print("Tran")

print("American development team")


time.sleep(3)