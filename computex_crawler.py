from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()

computex_url = "https://www.computextaipei.com.tw/zh-tw/exhibitor/show-area-data/index.html"
computex_url += "?pageSize=100"
driver.get(computex_url)

vip_venders = driver.find_elements(By.CLASS_NAME, "vip")

for vender in vip_venders:
    vender_name = vender.find_element(By. TAG_NAME, "h3")
    spans = vender.find_elements(By.XPATH, './/ul/li/span')
    ps = vender.find_elements(By.XPATH, './/ul/li/p')
    tags = vender.find_elements(By.XPATH, './/ul/li/a')  # . 從當前往下找
    print("<span>: ", [span.texr for span in spans])
    print("<p>: ", [p.text for p in ps])
    print("Tags: ", [tag.text for tag in tags])
    print()
