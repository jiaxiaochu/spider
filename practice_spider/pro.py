# # 导入Series
# from pandas import Series,DataFrame
#
# # 创建Series，使用默认索引
# sel =  Series(data=[1,'TheShy',20,'天不生theshy，LPL上单万古如长夜'])
# print(sel)

# 导入Series
# from pandas import Series,DataFrame
#
# # 创建Series，使用自定义索引
# sel =  Series(data=[1,'TheShy',20,'天不生theshy，Lpl上单万古如长夜'],
#               index = ['排名','ID号','年龄','评语'])
# print(sel)

# from pandas import Series,DataFrame
#
# # 将字典转换为Series
# dic={"red":100,"black":400,"green":300,"pink":900}
# se2=Series(data=dic)
# print(se2)
#
# from pandas import Series, DataFrame
#
# # 创建二维列表存储选手信息
# lol_list = [['上单', 'TheShy', 20],
#             ['打野', '小天', 19],
#             ['中单', 'Faker', 23],
#             ['ADC', 'Uzi', 22],
#             ['辅助', 'Ming', 21]]
# # 创建dataframe
# df = DataFrame(data=lol_list)
# print(df)


# from pandas import Series, DataFrame
#
# # 创建二维列表存储选手信息
# lol_list = [['上单', 'TheShy', 20],
#             ['打野', '小天', 19],
#             ['中单', 'Faker', 23],
#             ['ADC', 'Uzi', 22],
#             ['辅助', 'Ming', 21]]
# # 创建dataframe
# df = DataFrame(data=lol_list,
#                index=['a', 'b', 'c', 'd', 'e'],
#                columns=['位置', 'ID号', '年龄'])
# print(df)


from pandas import Series,DataFrame
import pandas as pd
# 使用字典创建
dic={
    '位置': ['上单', '打野', '中单', 'ADC', '辅助'],
    'ID号': ['TheShy', '小天', 'Faker', 'Uzi', 'Ming'],
    'year': [20, 19, 23, 22, 21]}
df = pd.DataFrame(dic)
print(df)
