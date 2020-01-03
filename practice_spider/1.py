# # !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# # -*- coding:utf-8 -*-
# # @Author : Jiazhixiang
# import requests
# from bs4 import BeautifulSoup
#
# # headers = {'user-agent': ''}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
# }
# res = requests.get('http://www.xiachufang.com/explore/', headers=headers)
# print(res.status_code)
# Soup = BeautifulSoup(res.text, 'html.parser')
# foods = Soup.find_all(class_='normal-recipe-list')
# # print(foods)
# list_all = []
# for food in foods:
#     tag_a = food.find('p', class_="name").find('a').text.replace(' ', '').replace('\n', '')
#     print(tag_a)
#     # name = tag_a.text.replace(' ', '').replace('\n', '')
#     # url = tag_a('a')['href']
#     # content_a = food.find(class_='ing ellipsis')
#     # content = content_a.text.replace(' ', '').replace('\n', '')
#     # list_all.append([name, url, content])
#     # list_all.append([tag_a, url, content])
#
# # print(list_all)


mylist = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
myset = set(mylist)  # myset是另外一个列表，里面的内容是mylist里面的无重复 项
for item in myset:
    print("the %d has found %d" % (item, mylist.count(item)))
print("#"*20)
List = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
a = {}
for i in List:
    if List.count(i) > 1:
        a[i] = List.count(i)
print(a)
