# 数据类型回顾

# 1.字符串     str
# 2.整形       int
# 3.浮点类型    float


# 列表   list
# 字典   dict

# 切片的语法：[起始:结束:步长]
# data = "abcdef"
# # 取出a
# print(data[0])
# # 取出d
# print(data[3])
# # 取出f
# print(data[5])

# data = "abcdef"
# 取出abc
# print(data[0:3])
# 取出 ace
# print(data[0:6])   # print(data)  # print(data[::])
# print(data[::3])
# 倒序
# print(data[::-1])

# 切片的语法：[起始:结束:步长]

# data = ["a", "b", "c", "d", "e", "f"]
# 取出b
# print(data[1])
# 取出abc
# print(data[0:3])
# 取出ace
# print(data[::2])


# list.append()   列表末尾追加数据

# data = ["a", "b", "c", "d", "e", "f"]
# print(type(data))
# 把hello添加到data当中
# print("======增加元素之前======")
# print(data)
# print("======增加元素之后======")
# data.append("hello")
# print(data)
# print("*" * 99)
# # insert()   指定位置增加元素
# # insert(index,object)  在指定位置index前插入袁术object
# print("======insert()增加元素之前======")
# print(data)
# print("======insert()增加元素之后======")
# data.insert(2, "world")
# print(data)
# print("*" * 99)


# 讲一个列表当中的元素逐个增加到另一个元素当中
# data1 = ["a", "b", "c"]
# data2 = ["d", "e", "f"]
# # data1.append(data2)
# # print(data1)
# # data = ["a", "b", "c", "d", "e", "f"]
# # data = ['a', 'b', 'c', ['d', 'e', 'f']]
# data2_1 = data2[0]
# # print(data2_1)
# data1.append(data2_1)
# print(data1)

# del list[元素的索引]
# data = ["a", "b", "c", "d", "e", "f"]
# print("======del 删除元素之前======")
# print(data)
# print("======del 删除元素之前======")
# del data[2]
# print(data)

# pop：删除最后一个元素
# data = ["a", "b", "c", "d", "e", "f"]
# print("======pop 删除元素之前======")
# print(data)
# print("======pop 删除元素之后======")
# data.pop()
# print(data)


# dict{"键":"值"}   由键值对组成
info = {'name': '李佳琦', 'age': 18}
#          键：值，           键：值
#          key:value       key:value
# print(info, type(info))
# 字典名[字典的键]，提取出来的是key对应的value
# print(info['name'])
# print(info['age'])
# 字典名[键] = 值，每次只能新增一个键值对
# info['height'] = 198
# print(info)
# 通过key找到元素位置，变量[键] = 新值
# info['age'] = 24
# print(info)

# del 字典名[键]
print("======del 删除元素之前======")
print(info)
print("======del 删除元素之后======")
del info['age']
print(info)
