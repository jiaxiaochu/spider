import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

tag_name = bs_foods.find_all('p',class_='name')
# print(tag_name)
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
list_all = []
for x in range(len(tag_name)):
    list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    list_all.append(list_food)
print(list_all)
