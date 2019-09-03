# -*- coding: utf-8 -*-
import scrapy
from redis import Redis
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ZlspcItem


class MoviesSpider(CrawlSpider):
    name = 'movies'

    start_urls = ['https://www.4567tv.tv/index.php/vod/show/id/5/page/1.html']

    rules = (
        Rule(LinkExtractor(allow=r'vod/show/id/5/page/\d+.html'), callback='parse_item', follow=True),
    )
    conn = Redis(host='localhost', port=6379)

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/div/h4/a/text()').extract_first()
            url = 'https://www.4567tv.tv/' + li.xpath('./div/a/@href').extract_first()
            item = ZlspcItem()
            item['title'] = title
            if self.conn.sadd('url', url):
                yield scrapy.Request(url=url, callback=self.parse_detail, meta={'item': item})
            else:
                print('当前%s数据已经获取...' % url)

    def parse_detail(self, response):
        item = response.meta['item']
        detail = response.xpath('/html/body/div[1]/div/div/div/div[2]/p//text()').extract()
        detail = ''.join(detail)
        item['detail'] = detail
        yield item
