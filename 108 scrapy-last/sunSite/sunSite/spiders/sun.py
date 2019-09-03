# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import SunsiteItem


class SunSpider(CrawlSpider):
    name = 'sun'
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    link = LinkExtractor(allow=r'question/\d+/\d+.shtml')
    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), callback='parse_item', follow=True),
        Rule(link, callback='parse_detail'),
    )

    def parse_item(self, response):
        item = {}
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            url = tr.xpath('./td[2]/a[2]/@href').extract_first()
            # print(title, url)
        yield item

    def parse_detail(self, response):
        num = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        title = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[1]/text()').extract_first()
        print(num)
        item = SunsiteItem()
        item['num'] = num
        item['title'] = title
        yield item
