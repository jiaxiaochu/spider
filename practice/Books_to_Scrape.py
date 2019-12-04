import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# content = soup.find(class_="product_pod")
# print(content)

content = soup.find_all(class_="product_pod")
for item in content:
    href = item.find('a')
    price = item.find(class_="price_color")
    instock = item.find(class_="instock availability")
    # print(href.text, '\n', price.text, '\n', instock.text)
    print(href.text, price.text, instock.text)
