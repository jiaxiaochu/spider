# class Musician:
#     glasses = "墨镜"
#     """定义了一个Muksician类"""
#
#     # Python 的类里提供的，两个下划线开始，两个下划线结束的方法，就是__init__()初始化¬方法，通常用来做属性初始化 或 赋值 操作。
#     # 如果类面没有写__init__方法，Python会自动创建，但是不执行任何操作，
#     # 如果为了能够在完成自己想要的功能，可以自己定义__init__方法，
#     # 所以一个类里无论自己是否编写__init__方法 一定有__init__方法。
#
#     def __init__(self, city):
#         """ __init__方法，用来做变量初始化 或 赋值 操作，在类实例化对象的时候，会被自动调用"""
#         self.city = city
#         print('组织语言中……')
#
#     def intr(self):
#         """实例方法"""
#         print('我来自%s' % self.city)
#
#
# # 实例化了一个Musician对象，并自动调用__init__()方法
# hebe = Musician('中国台湾')
# print(hebe.glasses)
#
# # 通过.成员进行选择，获取对象的实例方法
# hebe.intr()  # 只需要调用实例方法intr()，即可获取Musician的属性
#
#
# # __init__()方法，在创建一个对象时默认被调用，不需要手动调用
# # __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去。


import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
num = 0
for x in range(1, 4):
    params = {
        "ct": "24",
        "qqmusic_ver": "1298",
        "remoteplace": "txt.yqq.lyric",
        "searchid": "91372938206322439",
        "aggr": "0",
        "catZhida": "1",
        "lossless": "0",
        "sem": "1",
        "t": "7",
        "p": x,
        "n": "5",
        "w": "五月天",
        "g_tk": "5381",
        "loginUin": "0",
        "hostUin": "0",
        "format": "json",
        "inCharset": "utf8",
        "outCharset": "utf - 8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "0"
    }
    res = requests.get(url, params=params, headers=headers)
    dic = res.json()
    list = dic["data"]["lyric"]["list"]

    with open("lyric.txt", "a") as f:
        for songs in list:
            name = songs["songname"]
            lyric = songs["content"]#.replace(' ', '').replace('\n', '')
            num += 1
            # content = " % d.歌曲名字：【 % s】\n歌词： % s\n\n " % (num, name, lyric)
            # f.write(content)
            # print(content)
            # data = "% d.歌曲名字：%s22\n歌词：%s33\n " % (num, name, lyric)
            # print(name + "\n" + lyric)
            print(lyric)
            print("#"*77)
            print(lyric)
