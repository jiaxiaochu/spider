# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header


def get_weather():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101090601.shtml'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    bsdata = BeautifulSoup(res.text, 'html.parser')
    data_temperature = bsdata.find(class_='tem').text
    data_weather = bsdata.find(class_='wea').text
    return data_temperature, data_weather


def send_email(tem, wea, sender, pwd, recevier):
    mailhost = 'smtp.163.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(sender, pwd)
    content = '亲爱的，今天的天气是：' + tem + wea
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(sender, recevier, message.as_string())
        return True
    except Exception as e:
        return False
    # else:
    #     qqmail.quit()


def job():
    print('开始一次发送任务')
    tem, wea = get_weather()
    # sender = '1427369427@qq.com'
    # pwd = 'vurtxymnkgyfgjff'
    # recevier = '3068314778@qq.com'
    sender = 'hellojiazhixiang@163.com'
    pwd = 'jiazhixiang10712'
    recevier = '1072022525@qq.com'
    IsSuccess = send_email(tem, wea, sender, pwd, recevier)  # 这里需要设置发件人的账号密码以及收件人的账号
    while IsSuccess is False:
        print("邮件发送失败，正在尝试重新发送")
        IsSuccess = send_email(tem, wea, sender, pwd, recevier)
    print('任务完成')

job()
# schedule.every().day.at("18:17").do(job)
#
# while True:
#     schedule.run_pending()
#
#     time.sleep(1)
