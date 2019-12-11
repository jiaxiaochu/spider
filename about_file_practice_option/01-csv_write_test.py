# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import csv

with open("../source/source_file/demo.xlsx", "w", encoding='utf-8')as file:
    writer = csv.writer(file)
    writer.writerow(['电影', '豆瓣评分'])
    writer.writerow(['银河护卫队', '8.0'])
    writer.writerow(['复仇者联盟', '8.1'])
