# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from redis import Redis


class QiubaiPipeline(object):
    fp = None

    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('qiubai.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content)
        return item

    def close_spider(self, spider):
        print('结束爬虫')
        self.fp.close()


class MysqlPL(object):
    con = None
    cursor = None

    def open_spider(self, spider):
        print('*' * 32)
        self.con = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='spider',
                                   charset='utf8')
        print(self.con)

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        sql = 'insert into qiubai values ("%s", "%s")' % (author, content)
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        return item

    def close_spider(self, spider):
        print(self.cursor, self.con)
        self.cursor.close()
        self.con.close()


class MyRedis(object):
    con = None

    def open_spider(self, spider):
        self.con = Redis(host='127.0.0.1', port=6379, db=1)
        print(self.con)

    def process_item(self, item, spider):
        self.con.lpush('data', item)
        return item


