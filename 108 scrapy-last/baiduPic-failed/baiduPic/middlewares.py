# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from time import sleep


class BaidupicDownloaderMiddleware(object):

    def process_request(self, request, spider):
        if request.url == 'http://pic.netbian.com/4kmeinv/':
            bro = spider.bro
            bro.get(request.url)
            sleep(1)
            bro.find_element_by_xpath('/html/body/div[1]/div/div[2]/a[2]').click()


            return None
