# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# @Time : 2019/12/6


import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
start_url = "https://movie.douban.com/top250?start=0&filter="
res = requests.get(start_url, headers=headers)
response = BeautifulSoup(res.text, 'html.parser')
data = response.find_all('ol', class_="grid_view")
content = response.find_all('li')
for item in content:
    # print(item)
    '''
        查找序号    num
        查找电影名   move_name
        查找推荐语   recommend
        查找评分    score
        连接  link
    '''
    # try:
    #     num = item.find('em', class_="").text
    #     if num is None:
    #         break
    # except:
    #     print("error")
    num = item.find('em', class_="")
    move_name = item.find('span', class_="title").text
    recommend = item.find('span', class_="inq").text
    score = item.find('span', class_="rating_num").text
    link = item.find('a')['href']
    print(num.text + move_name + recommend + score + link)
