import requests
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
start_url = "http://www.xiachufang.com/explore/"
response = requests.get(start_url, headers=headers)
html = response.text
# with open('../source/source_file/1.txt', 'w')as file:
#     file.write(html)
soup = BeautifulSoup(html, 'html.parser')
# with open('../source/source_file/2.txt', 'w')as file:
#     file.write(str(soup))
# print(type(soup))
content = soup.find_all('div', class_="info pure-u")
# print(content)
for item in content:
    food_name = item.find('p')
    link = item.find('a')
    material = item.find(class_="ing ellipsis")
    do_time = item.find(class_="stats green-font")
    who_did = item.find(class_="author")
    print(food_name.text, '\n', 'http://www.xiachufang.com' + link['href'], '\n', material.text, '\n', do_time.text,
          '\n', who_did.text)
