# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import WangyiItem

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['https://news.163.com']
    bro = webdriver.Chrome(executable_path='/Users/henry/Downloads/Tools/chromedriver', chrome_options=chrome_options)
    url_list = []

    def parse(self, response):
        url_index = [3, 4, 6, 7, ]
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        for index in url_index:
            url = li_list[index].xpath('./a/@href').extract_first()
            self.url_list.append(url)
            if url:
                yield scrapy.Request(url, self.parse_news)

    def parse_news(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div/h3/a/text()').extract_first()
            detail_url = div.xpath('./div/div/h3/a/@href').extract_first()
            item = WangyiItem()
            item['title'] = title
            print(detail_url)
            if detail_url:
                yield scrapy.Request(detail_url, self.parse_content, meta={'item': item})
            else:return

    def parse_content(self, response):
        # print('****' * 8)
        item = response.meta.get('item')
        content = response.xpath('//*[@id="endText"]/p/text()').extract()
        content = ''.join(content)
        item['content'] = content
        # print(item)
        yield item

    def close(self, spider):
        self.bro.quit()
