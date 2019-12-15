# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()   # 定义书名的属性
    publish = scrapy.Field()   # 定义出版信息的属性
    score = scrapy.Field()     # 定义书籍的评分属性
    recommend = scrapy.Field()  # 定义书籍的推荐语属性

