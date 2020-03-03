import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
res = requests.get('http://www.xiachufang.com/explore/', headers=headers)
bs = BeautifulSoup(res.text, 'html.parser')
t_name = bs.find_all('p', class_='name')
sc = bs.find_all('p', class_='ing ellipsis')
list_all = []
for food in range(len(t_name)):
    list_food = [t_name[food].text[18:-14], t_name[food].find('a')['href'], sc[food].text[1:-1]]
    list_all.append(list_food)
print(list_all)
