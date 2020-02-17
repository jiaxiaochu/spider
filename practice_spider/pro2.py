# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
headers={
'origin':'http://y,qq.com',
'referer':'http://yqq.com/n/yqq/song/004Z8Ihr0JIu5s',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
for i in range(1,4):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    param={
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '56285726861689722',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': i,
        'n': '10',
        'w': '五月天',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf - 8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
}
    res_songs=requests.get(url,params=param,headers=headers)
    json_songs=res_songs.json()
    list_songs=json_songs['data']['song']['list']
    url_1='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    for music in list_songs:
        name = music['name']
        param_lyric={
            'nobase64': '1',
            'musicid': str(music['id']),
            '-': 'jsonp1',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
        headers = {
'origin' : 'http://y,qq.com',
'referer' : 'http://yqq.com/n/yqq/song/004Z8Ihr0JIu5s',
'user-agent':'Mozilla/5.0(WindowsNT 6.1;Winx64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/77.0.3865.90 Safari/537.36,'
}
        res_lyric = requests.get(url_1,params=param,headers=headers)
        json_lyric=res_lyric.json()
        lyric=json_lyric['lyric']
# print(name,lyric)
print([name, lyric])
