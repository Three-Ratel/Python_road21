# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    addr = scrapy.Field()
    field = scrapy.Field()
    position_name = scrapy.Field()
    direction = scrapy.Field()
    salary = scrapy.Field()
    education = scrapy.Field()
    work_year = scrapy.Field()
    desc = scrapy.Field()
    requirements = scrapy.Field()
    company_size = scrapy.Field()

