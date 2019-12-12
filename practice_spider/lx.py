# for 变量 in 列表：
#         使用变量

# name_list = ['zhangsan', 'lisi', 'wangwu']  # 列表  3个元素
# # print(name_list, type(name_list))
# for name in name_list:  # 列表当中必有3个元素
#     print(name)

# for循环遍历列表
# name_list = ['zhangsan', 'lisi', 'wangwu', 'xiaoming', 'xiaohong']  # 列表  5个元素
# # print(name_list, type(name_list))
# for i in name_list:  # 列表当中必有5个元素
#     print(i)


# 使用while循环遍历列表
# i = 0
#     while i<len(列表):
#         使用列表中的元素(列表[i])
#         i += 1
#
# name_list = ['zhangsan', 'lisi', 'wangwu', 'xiaoming', 'xiaohong']  # 列表  5个元素
# # len()  统计李彪当中有多少个元素
# # print(len(name_list))
# length = len(name_list)
# # print(length)
# i = 0
# while i < length:  # 条件满足，
#     print(name_list[i])  # 条件满足，要执行的代码
#     i = i + 1  # i +=1


# 使用for循环遍历字典
# name_list = {'name': 'zhangsan', "age": 30}  # < class 'dict'>  2个键值对
#               key:value          key: value
# print(name_list, type(name_list))
# 遍历字典的key（键）
# for key in name_list:
#     print(key)
# 扩展知识
# for key in name_list.keys():
#     print(key)
# for key in name_list.values():
#     print(key)

# 遍历字典的key-value(键值对)
# for 变量i，变量j in 字典.items()：
#         使用变量i遍历所有键，通过变量j遍历所有值
# name_list = {'name': 'zhangsan', "age": 30}  # < class 'dict'>  2个键值对
# # 字典.items()：
# # print(name_list.items())
# for key, value in name_list.items():
#     print("key=%s,value=%s" % (key, value))


# range()函数

# rang(start,stop,step)
# start：计数从start开始。默认是从0开始，例如range(5)   等价于  range(0,5)
# stop:计数到stop结束，但不包括stop。列如range（0，5）  是  [0,1,2,3,4]没有5
# step:步长，默认是1。例如range(0,5)等价于range(0,5,1)
# for i in range(10):
#     print(i)


# 算术运算符

# print(1+2)
# a = 7
# b = 3
# a ！= b
# c = a//b
# print(2**2)
# result = 3*5
# print(result)


# and  与
# a = 10
# b = 20
# print(a and b)   # and:左右表达式都为True,则整个表达式结果为True
# # 如果X为false，x and y 返回False,否则它返回y的值：
# if (1 == 1) and (10>3):
#     print("条件成立")

# or 或
# or：左右表达式有一个为True，整个表达式结果为True
# 如果X是true,他返回true,否则返回Y的值。
# if (1 == 2) or (10 >3):
#     print("条件成立")


# not  布尔非
# not true 返回 False,not False 返回True
# 如果X为True,返回false。如果x为False,它返回true。
# if not (1 == 2):
#     print("条件成立")


# i = 0
# while i < 5:
#     i = i + 1
#     print("____分隔符_____")
#     if i == 3:
#         break
#         # print("满足i == 3的条件执行的代码")
#     print(i)
# else:
#     print("==while循环过程中，如果没有执行break退出，则执行本语句==")
# # break的作用：立刻结束break所在的循环

# break的作用：立刻结束break所在的循环
# continue的作用：用来结束本次循环，紧接着执行下一次的循环
name = 'xiaoming'
for i in name:
    print("____分隔符_____")
    if i == 'm':
        continue
    print("跳出循环时i的值是：%s" % i)
else:
    print("==for循环过程中，如果没有执行break退出，则执行本语句==")
# break的作用：立刻结束break所在的循环
# continue的作用：用来结束本次循环，紧接着执行下一次的循环
