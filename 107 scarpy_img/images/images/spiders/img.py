# -*- coding: utf-8 -*-
import scrapy

from ..items import ImagesItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    start_urls = ['http://www.xiaohuar.com/hua/']
    url = 'http://www.xiaohuar.com/list-1-%d.html'
    page = 1

    def parse(self, response):
        div_list = response.xpath('//*[@id="list_img"]/div/div[1]/div')
        for div in div_list:
            src = div.xpath('./div/div/a/img/@src').extract_first()
            item = ImagesItem()
            item['src'] = 'http://www.xiaohuar.com' + src
            # print(item)
            yield item

        if self.page < 3:
            self.page += 1
            yield scrapy.Request(url=self.url % self.page, callback=self.parse)
