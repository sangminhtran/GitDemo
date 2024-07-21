import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get('https://rahulshettyacademy.com/angularpractice/')

# a[href*='shop'] là CSS Selector lấy element có attribute có giá trị khớp 1 phần
# //a[contains(@href,'shop')] là Xpath lấy element có attribute có giá trị khớp 1 phần
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, 'div/h4/a').text
    if productName == 'Blackberry':
        product.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
# có thể ko xài tag name, với Xpath thì //*[attribute]

successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText



time.sleep(3)
