# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def parse(self, response):
        pass
