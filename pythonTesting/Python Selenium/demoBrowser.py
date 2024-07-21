import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome()  # tạo obj driver từ class selenium, Chrome driver service

# trường hợp cty sử dụng VPN thì nên dùng Service get path của chrome driver download tay về
# với FireFox thì download gecko driver
service_obj = Service('/Users/sangtran/Desktop/Sang Place/Study/Selenium Python/Selenium project/Webdriver/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://google.com')     # đi tới trang web
driver.maximize_window()
print(driver.title)                # print title của web
print(driver.current_url)            # print url của web hiện tại

print("Hello1")
print("Hello2")
print("Hello3")

time.sleep(2)                # sau khi run xong selenium sẽ tự đóng browser nên cần time delay