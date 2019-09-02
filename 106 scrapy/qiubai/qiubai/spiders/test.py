# -*- coding: utf-8 -*-
import scrapy

from ..items import QiubaiItem


class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/hot/', ]
    page = 1
    url = 'https://www.qiushibaike.com/hot/page/%d/'

    def parse(self, response):
        div_list = response.xpath('//*[@id="content-left"]/div')
        for div in div_list:
            author = div.xpath('./div/a/h2/text()').extract_first()
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)
            item = QiubaiItem()
            item['author'] = author if author else '匿名'
            item['content'] = content
            yield item

        if self.page < 10:
            self.page += 1
            new_url = self.url % self.page
            print(new_url)
            yield scrapy.Request(new_url, callback=self.parse)
