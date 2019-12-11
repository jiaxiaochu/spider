# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# @Time : 2019/12/11

import csv

with open("../source/source_file/demo.xlsx", "r", encoding='utf-8')as file:
    reader = csv.reader(file)
    print(reader)
    for content in reader:
        print(content)
