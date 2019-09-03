# -*- coding: utf-8 -*-

from random import random

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PicSpider(CrawlSpider):
    name = 'pic'
    start_urls = ['http://pic.netbian.com/4kmeinv/']
    pic_link = LinkExtractor(allow='/tupian/\d+.html')
    rules = (
        Rule(LinkExtractor(allow=r'/4kmeinv/index_\d+.html/'), callback='parse_item', follow=True),
        Rule(pic_link, callback='parse_pic'),
    )

    def parse_item(self, response):
        yield

    def parse_pic(self, response):
        yield

    def parse_download(self, response):
        _id = response.xpath('//*[@id="main"]/div[2]/div[2]/div[1]/a/@data-id').extract_first()
        url = '/e/extend/downpic.php?id=' + _id + '&t=' + random()
        yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        print(response.pic)
        yield

    # '/e/extend/downpic.php?id=' + id + '&t=' + Math.random()
    # window.location.href = data.pic

