# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import requests
from bs4 import BeautifulSoup

start_url = "http://product.dangdang.com/24047480.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding
print(response.status_code, response.encoding)
soup = BeautifulSoup(response.text, 'html.parser')
datas = soup.find_all('div', class_="product_wrapper")
author_info = soup.find_all('span', id='author')
classify = soup.find_all('div', class_="breadcrumb", id="breadcrumb", dd_name="顶部面包屑导航")

for data in datas:
    book_name = data.find('div', class_="name_info").find('h1')['title']  # .replace(' ', '').replace('\n', '')
    # book_author1 = data.find('span', id="author").find('a', target="_blank")
    book_publish_info = data.find('span', dd_name="出版社").text
    # book_publish_time = data.find('span', class_="messbox_info")
    print("书名：{},出版社：{}".format(book_name, book_publish_info))

for item in author_info:
    author1 = item.find_all('a', target="_blank")[0].text
    author2 = item.find_all('a', target="_blank")[1].text
    author3 = item.find_all('a', target="_blank")[2].text
    print("作者：{}".format(author1 + author2 + author3))

price_info = soup.find('div', class_="price_pc", id="pc-price")
# 定价
origin_price = price_info.find('div', class_="price_m", id="original-price").text
# 刷新页面瞬间变化值price
p_price = price_info.find('div', class_="price_d").find('p', id="dd-price").text
# 折扣
discount = price_info.find('div', class_="price_zhe", id="dd-zhe").text
# print("折扣：{}".format(discount))
# 刷新页面瞬间变化值price
# price = data.find('div', class_="price_d").find('p', id="dd-price").text
print("定价：{}".format(origin_price))
print("刷新页面瞬间变化价格：{}".format(p_price))
print("折扣：{}".format(discount))

for sort in classify:
    c1 = sort.find_all('a')[0].text
    c2 = sort.find_all('a')[1].text
    c3 = sort.find_all('a')[2].text
    c4 = sort.find_all('a')[3].text
    print("类别：{}".format(c1))
    print("二级分类：{}".format(c2))
    print("三级分类：{}".format(c3))
    print("四级分类：{}".format(c4))

yidong_discount = soup.find('span', class_="discount")
print(yidong_discount)
