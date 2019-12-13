# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

link = 'https://www.xslou.com/yuedu/9356/'

# 字符串link过滤出数字id（9356）
id_list = list(filter(str.isdigit, link))
book_id = ''.join(book_id)

# 步骤解析：1、filter()过滤数字 2、filter对象转列表 3、列表转字符串
# filter(str.isdigit,字符串)
# 第一个参数用来判断字符串的单个元素是否是数字，数字保留
# filter()返回的是对象，需要用list()函数转换成列表
# ''.join(列表)将列表转换成字符串
