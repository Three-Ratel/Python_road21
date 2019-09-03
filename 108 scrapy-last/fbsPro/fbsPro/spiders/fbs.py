# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider

from ..items import FbsproItem


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    # 表示的是可被共享调度器中队列的名称
    redis_key = 'fbsQueue'
    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            status = tr.xpath('./td[3]/span/text()').extract_first()
            item = FbsproItem()
            item['title'] = title
            item['status'] = status
            yield item
