# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class SunSpider(RedisCrawlSpider):
    name = 'sun'

    redis_key = 'sentinelQueue'
    # start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    link = LinkExtractor(allow=r'type=4&page=\d+')
    link_content = LinkExtractor(allow=r'question/\d+/\d+.shtml')

    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_content, callback='parse_content', ),
    )

    def parse_item(self, response):
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            tr.xpath('./td[2]/a[2]/@href').extract_first()

    def parse_content(self, response):
        item = {}
        num = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        title = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[1]/text()').extract_first()
        print(title)
        # item['num'] = num
        item['title'] = title
        yield item
