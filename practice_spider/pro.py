import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = '1030135838@qq.com'  # input('请输入你的邮箱：')
password = 'mqubgmhqeilnbahf'  # input('请输入你的密码：')
receiver = '1072022525@qq.com'  # input('请输入收件人的邮箱：')
index = 0


def movie_spider():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    url = 'https://at.alicdn.com/t/font_1358396_idad7a5g6ir.css'
    res_movies = requests.get(url, headers=headers)
    bs_movies = BeautifulSoup(res_movies.text, 'html.parser')
    list_movies = bs_movies.find_all('div', class_='pl2')
    list_all = []
    for movie in list_movies:
        tag_a = movie.find('a')
        name = tag_a.text.replace(' ', '').replace('\n', '')
        url = tag_a['href']
        tag_p = movie.find('p', class_='pl')
        information = tag_p.text.replace(' ', '').replace('\n', '')
        tag_div = movie.find('div', class_='star clearfix')
        rating = tag_div.text.replace(' ', '').replace('\n', '')

        list_all.append(name + url + information + rating)
    return list_all

def send_email(movie_list):
    global account, password, receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(account, password)
    content = '测试测试测试测试\n'.join(movie_list)
    print(content, "@@测试content测试@@")
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '本周豆瓣新片榜'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()


def job():
    global index
    print('开始任务')
    movie_list = movie_spider()
    send_email(movie_list)
    print(movie_list)
    print('任务完成')
    index += 1


schedule.every().second.do(job)

while index != 2:
    schedule.run_pending()
    time.sleep(1)
