# -*- coding: utf-8 -*-
import json
from time import sleep

import scrapy

from ..items import LagouItem


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.lagou.com/jobs/list_python/p-city_2', ]

    def parse(self, response):
        for i in range(1, 3):
            print(f'正在爬取第{i}页....')
            data = {'first': 'true', 'pn': str(i), 'kd': 'python'}
            url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false'
            yield scrapy.FormRequest(url, formdata=data, callback=self.parse_company)
            sleep(20)
            print(f'第{i}页爬取结束!')

    def parse_company(self, response):
        res_dict = json.loads(response.text)
        '公司名称、公司地址、公司类型领域、岗位名称、python方向、薪资、学历、经验、职位描述、任职要求、公司规模'
        company_list = res_dict['content']['positionResult']['result']
        for company_dict in company_list:
            item = LagouItem()
            item['company_name'] = company_dict['companyFullName']
            item['field'] = company_dict.get('industryField')
            item['position_name'] = company_dict.get('positionName')
            item['direction'] = company_dict.get('secondType')
            item['salary'] = company_dict.get('salary')
            item['education'] = company_dict.get('education')
            item['work_year'] = company_dict.get('workYear')

            position_id = company_dict.get('positionId')
            show_id = res_dict['content']['showId']
            url = f'https://www.lagou.com/jobs/{position_id}.html?show={show_id}'
            yield scrapy.Request(url=url, meta=item, callback=self.parse_detail)

            # company_info['addr'] = company_dict.get('addr')
            # company_info['desc'] = company_dict.get('workYear')
            # company_info['requirements'] = company_dict.get('workYear')
            # company_info['company_size'] = company_dict.get('workYear')

    def parse_detail(self, response):
        res = json.loads(response.text)
        print(res)