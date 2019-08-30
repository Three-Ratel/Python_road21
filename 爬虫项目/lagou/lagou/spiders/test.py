# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['https://www.lagou.com/jobs/list_python?px=default&city=北京']
    start_urls = ['https//www.lagou.com/jobs/list_python', ]

    def parse(self, response):
        print(response)
