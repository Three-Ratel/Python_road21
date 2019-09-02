# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImagePL(ImagesPipeline):
    print('here')

    def get_media_requests(self, item, info):
        print(item['src'])
        print('get_media_requests')
        yield scrapy.Request(item['src'])

    def file_path(self, request, response=None, info=None):
        print('file_path')
        name = request.url.split('/')[-1]
        print('正在下载：%s' % name)
        return name

    def item_completed(self, results, item, info):
        print('item_completed')
        return item
