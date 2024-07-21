import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')  # headless mode là chạy test ở chế độ ko có UI -> run nhanh hơn
chrome_options.add_argument('--ignore-certificate-errors')  # auto access website khi private connection error

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# execute javascript - scroll từ top đến cuối page
driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
driver.get_screenshot_as_file("screen.png")  # chụp hình browser save ở folder của file hiện tại

time.sleep(3)