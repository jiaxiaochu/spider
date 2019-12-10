# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# @Time : 2019/12/10

import requests
# 引用requests模块

for i in range(0,3):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+str(i*20)
    res_movie = requests.get(url)
    # 调用get方法，下载电影列表
    json_movie = res_movie.json()
    # 使用json()方法，将response对象，转为列表/字典
    # print(json_movie)
    list_movies = json_movie['subjects']
    # 一层一层地取字典，获取电影名称
    for comment in list_movies:
    # list_movies，comment是它里面的元素
        print(comment['title'])
    #     # 输出电影名名称
