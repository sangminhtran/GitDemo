from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('headless')  # headless mode là chạy test ở chế độ ko có UI -> run nhanh hơn
chrome_options.add_argument('--ignore-certificate-errors')  # auto access website khi private connection error

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj, options=chrome_options)


driver.get('https://rahulshettyacademy.com/angularpractice/')

print(driver.title)