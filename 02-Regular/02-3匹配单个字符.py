# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
'''

字符	功能
.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符

'''
# 示例3：\d
import re

# 普通的匹配方式
ret = re.match("嫦娥1号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥2号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥3号", "嫦娥3号发射成功")
print(ret.group())

print("*" * 77)
# 使用\d进行匹配
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())




# emp = {"name": "张三","age": "22", "sex": "男"}
# print(emp)  # {'name': '张三', 'age': '22', 'sex': '男'}
#
# v = emp.get("name")
# print(v)    # 张三
#
# emp["dept"] = "研发部"
# print(emp)  # {'name': '张三', 'age': '22', 'sex': '男', 'dept': '研发部'}
#
# kv = emp.popitem()
# print(emp)  # {'name': '张三', 'age': '22', 'sex': '男'}
# print(kv)   # ('dept', '研发部')
