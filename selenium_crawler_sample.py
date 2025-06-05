from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# webdriver.Firefox()
# webdriver.Safari()
# webdriver.Edge()
driver = webdriver.Chrome()

driver.get("http://www.selenium.dev/selenium/web/web-form.html")

print("Title:", driver.title)

# time.sleep(10)
# driver.implicitly_wait(0.5) 與上方功能相同

text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(By.CSS_SELECTOR, value="button")
submit_button = driver.find_element(By.TAG_NAME, value="button")

radio_default = driver.find_element(
    By.XPATH, '//label/input[@id="my-radio-2"]')
radio_default.click()
print("Default radio: ", radio_default.text)
# print("Default radio: ", radio_default.is_selected())
time.sleep(5)

text_box.send_keys("Selenium")
submit_button.click()

time.sleep(3)  # wait the browser to the next page
message = driver.find_element(by=By.ID, value="message")
text = message.text
print("Text:", text)
time.sleep(10)
driver.quit()
