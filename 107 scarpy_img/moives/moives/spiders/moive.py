# -*- coding: utf-8 -*-
import scrapy

from ..items import MoivesItem


class MoiveSpider(scrapy.Spider):
    name = 'moive'
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/class/动作/id/1.html']
    url = 'https://www.4567tv.tv/index.php/vod/show/id/5/page/%d.html'

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            detail_url = 'https://www.4567tv.tv' + li.xpath('./div/a/@href').extract_first()
            item = MoivesItem()
            item['title'] = title

            yield scrapy.Request(detail_url, callback=self.detail_parse, meta={'item': item})

    def detail_parse(self, response):
        item = response.meta.get('item')
        detail = response.xpath('/html/body/div[1]/div/div/div/div[2]//text()').extract()
        detail = ''.join(detail)
        item['detail'] = detail
        yield item
