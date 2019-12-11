# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# @Time : 2019/12/11

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
# params = {
#     "include": "data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics",
#     "offset": "10",
#     "limit": "10",
#     "sort_by": "voteups"
# }
start_url = "https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?"
offset = 0
list_all = []
while True:
    params = {
        "include": "data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics",
        "offset": str(offset),
        "limit": "10",
        "sort_by": "voteups"
    }
    response = requests.get(url=start_url, headers=headers, params=params)
    # print(response.status_code)
    # print(response.apparent_encoding)
    json_response = response.json()
    # print(type(json_response))
    data = json_response['data']
    for content in data:
        # title = content['title']
        # url = content['url']
        # excerpt = content['excerpt']
        # list_all.append([title, url, excerpt])
        # print(title, url, excerpt)
        list_data = [content['title'], content['url'], content['excerpt']]
        list_all.append(list_data)
    offset += 20
    # 如果offset大于40，即爬了两页，就停止,不给知乎服务器增加压力
    if offset > 40:
        break
    # if json_response['paging']['is_end'] == True:
    #     # 如果键is_end所对应的值是True，就结束while循环。
    #     break
print(list_all)
