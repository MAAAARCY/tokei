import requests
from bs4 import BeautifulSoup
import json

# スクレイピングしたいページのURL
url = "https://www.hulft.com/help/ja-jp/WebFT-V3/COM-ADM/Content/WEBFT_ADM_COM/TimeZone/timezonelist.htm"

# Webページの内容を取得
response = requests.get(url)

# レスポンスからHTMLをパース
soup = BeautifulSoup(response.content, 'html.parser')

# 例: ページ内のタイトルを取得
title = soup.find('title').text
print(f"ページタイトル: {title}")

# 例: 特定のクラスを持つ要素を取得
elements = soup.find_all(class_='TableStyle-H_Basic-Body-Body1')
timezones = dict()

ct = 0
for element in elements:
    timezone_info = element.text.splitlines()
    timezones[timezone_info[8].replace(' ', '')] = timezone_info[5]

with open('timezones.json', 'w', encoding="utf-8") as file:
    json.dump(timezones, file, ensure_ascii=False, indent=4) 
        