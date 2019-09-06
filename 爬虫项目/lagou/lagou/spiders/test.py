# -*- coding: utf-8 -*-
import json
from time import sleep

import scrapy
from scrapy.http.cookies import CookieJar

from ..items import LagouItem

HEADERS = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'refferer': 'https://www.lagou.com/jobs/list_python/p-city_2?px=default',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.lagou.com/jobs/list_python/p-city_2', ]
    # 实例化一个cookiejar对象
    cookie_jar = CookieJar()

    def parse(self, response):
        self.cookie_jar.extract_cookies(response, response.request)

        for i in range(1, 2):
            print(f'正在爬取第{i}页....')
            data = {'first': 'true', 'pn': str(i), 'kd': 'python'}
            url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false'
            yield scrapy.FormRequest(url, formdata=data, headers=HEADERS, callback=self.parse_company,)
            print(f'第{i}页爬取结束!')
            sleep(2)

    def parse_company(self, response):
        # print(response.text, '-' * 80)

        res_dict = json.loads(response.text)
        '公司名称、公司地址、公司类型领域、岗位名称、python方向、薪资、学历、经验、职位描述、任职要求、公司规模'

        company_list = res_dict['content']['positionResult']['result']
        urls = []
        show_id = ''
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
            url = f'https://www.lagou.com/jobs/{position_id}.html?show=%s'
            urls.append(url)
        for url in urls:
            url = url % show_id
            print(url)
            res = scrapy.Request(url, headers=HEADERS,)
            print(res.headers)
            with open('test.html', 'w', encoding='utf8') as f:
                f.write(str(res.body))
            break

            # headers = json.loads(res.headers)
            # show_id = headers.get('Request_Id')
            # tree = etree.HTML(res)
            # detail_info = tree.xpath('//*[@id="job_detail"]/dd[2]/div//text()')
            # print(detail_info)

            # company_info['addr'] = company_dict.get('addr')
            # company_info['desc'] = company_dict.get('workYear')
            # company_info['requirements'] = company_dict.get('workYear')
            # company_info['company_size'] = company_dict.get('workYear')
