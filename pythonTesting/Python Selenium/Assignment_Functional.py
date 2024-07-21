import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

# Thiết lập thời gian chờ ngầm cho đến khi trang web/element được load xong
# Nếu đợi 5s mà element xuất hiện sau 2s => chấm dứt 3s đợi
# Global timeout - apply toàn bộ
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)   # implicitly_wait ko work khi findElements (List) nên cần time.sleep
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)  # add item zô List
    result.find_element(By.XPATH, "div/button").click()  # find child element từ parent

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()  # chuyển page tiếp

# Sum validation (tính sum các giá trị của item trong bảng)
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)  # ép kiểu text -> int

print(sum)
totalAmount  = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit Wait, chỉ apply thời gian chờ cho 1 element chỉ định với điều kiện cụ thể
# update time ko ảnh hưởng đến Implicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalAmount > discountedAmount