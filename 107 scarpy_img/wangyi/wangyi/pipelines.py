# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from time import sleep

import pymysql

from .tools import BaiduAI


class WangyiPipeline(object):

    def open_spider(self, spider):
        print('*' * 32)
        # self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='spider',
        #                            charset='utf8')
        # self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        # print(title)

        # """ 调用文章分类 """
        res = BaiduAI.client.topic(title, content)
        sleep(0.5)
        lv1_tag_list = res.get('item').get('lv1_tag_list')
        if lv1_tag_list:
            tag = lv1_tag_list[0].get('tag')
            item['tag'] = tag
            print(item['title'], item['tag'], )

            # sql = f"insert into article value('{tag}', '{title}', '{content}')"
            # print(sql)
            # try:
            #     self.cursor.execute(sql)
            #     self.conn.commit()
            # except Exception as e:
            #     print(e)
            #     self.conn.rollback()

        return item

    def close_spider(self, spider):
        # print(self.cursor, self.conn)
        # self.cursor.close()
        # self.conn.close()
        pass
