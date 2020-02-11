import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
start_url = "http://www.xiachufang.com/explore/"
response = requests.get(start_url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find_all('div', class_="info pure-u")

for item in content:
    food_name = item.find('p').text.replace(' ', '').replace('\n', '')
    link = item.find('a')
    material = item.find(class_="ing ellipsis")
    do_time = item.find(class_="stats green-font")
    who_did = item.find(class_="author")
    print(food_name, '\n', 'http://www.xiachufang.com' + link['href'], '\n', material.text, '\n', do_time.text,
          '\n', who_did.text)


# dict_all = {}
# for item in content:
#     dict_all['food_name'] = item.find('p')
#     dict_all['link'] = item.find('a')
#     dict_all['material'] = item.find(class_="ing ellipsis")
#     dict_all['do_time'] = item.find(class_="stats green-font")
#     dict_all['who_did'] = item.find(class_="author")
#
# print(dict_all)



# tag_name = soup.find_all('p', class_='name')
# # print(tag_name)
# tag_ingredients = soup.find_all('p', class_="ing ellipsis")
# list_all = []   # 创建一个空列表，用于存储信息
# for i in range(len(tag_name)):
#     list_food = tag_name[i].text
#     print(list_food)
