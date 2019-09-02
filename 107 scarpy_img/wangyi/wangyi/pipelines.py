# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from time import sleep

from .tools import BaiduAI


class WangyiPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        print(title)

        # """ 调用文章分类 """
        # res = BaiduAI.client.topic(title, content)
        # sleep(0.5)
        # lv1_tag_list = res.get('item').get('lv1_tag_list')
        # if lv1_tag_list:
        #     tag = lv1_tag_list[0].get('tag')
        #     item['tag'] = tag
        #     print(item['title'], item['tag'], )

            # sql = f"insert into article value('{tag}', '{title}', '{content}')"
            # print(sql)
            # try:
            #     from .tools import databases
            #     databases.cursor.execute(sql)
            #     databases.conn.commit()
            # except Exception as e:
            #     print(e)
            #     databases.conn.rollback()

        return item
