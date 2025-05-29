# Step 1. 取回 HTML
from pprint import pprint
from bs4 import BeautifulSoup
import requests  # request 是一個 Module 做網路溝通用的
r = requests.get("https://www.twking.org")
r.encoding = "utf8"  # 處理亂碼

# Step 2. response
print(r.text)

# Step 3. 轉化成 Soup
soup = BeautifulSoup(r.text, "html.parser")

# Step 4. Analyst - 分析連結跟小說名稱 by 排行榜種類
booktop_data = dict()  # 資料儲存
booktops = soup.find_all("div", class_="booktop")  # return list of booktops
for booktop in booktops:
    booktop_name = booktop.p.string
    print(booktop_name)
    booktop_data[booktop_name] = [
        # 排行榜是Key，把[(小書連結及書名)]存成 Value
        (top["href"], top.string.strip()) for top in booktop.find_all("a")]
    # Top 10
    for top in booktop.find_all("a"):
        # print(top)
        print(top["href"], top.string.strip())  # 連結與小說名稱

pprint(booktop_data)
