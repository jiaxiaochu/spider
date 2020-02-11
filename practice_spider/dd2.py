from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 群发收件人地址:
to_addr = []
while True:
    addr = input('请输入收件人邮箱地址To: ')
    to_addr.append(addr)
    res = input('是否继续，输入1加邮箱，其他结束')
    if res == '1':
        continue
    else:
        break

content = '''
亲爱的学员朋友：
    你好！
 恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'蒋<%s>' % from_addr)
msg['To'] = _format_addr(u'静趣无为 <%s>' % to_addr)
msg['Subject'] = Header(u'来自亿家公寓……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
