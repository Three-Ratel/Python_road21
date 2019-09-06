from time import sleep

import requests
from requests import Session


class Lagou(object):
    session = Session()
    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    data = {
        'first': True,
        'pn': '1',
        'kd': 'Python',
    }
    show_id = ''
    urls = []

    def get_show_id(self):
        res = self.session.get('https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC',
                               headers=self.headers)
        self.show_id = res.headers.get('REQUEST_ID')

    def get_first_page(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false'
        response = self.session.post(url=url, data=self.data, headers=self.headers).json()

        '公司名称、公司地址、公司类型领域、岗位名称、python方向、薪资、学历、经验、职位描述、任职要求、公司规模'
        company_list = response['content']['positionResult']['result']

        for company_dict in company_list:
            item = {}
            item['company_name'] = company_dict['companyFullName']
            item['field'] = company_dict.get('industryField')
            item['position_name'] = company_dict.get('positionName')
            item['direction'] = company_dict.get('secondType')
            item['salary'] = company_dict.get('salary')
            item['education'] = company_dict.get('education')
            item['work_year'] = company_dict.get('workYear')

            position_id = company_dict.get('positionId')
            self.show_id = response['content']['showId']
            url = f'https://www.lagou.com/jobs/{position_id}.html?show=%s'
            self.urls.append(url)

    def get_detial_page(self):
        for url in self.urls:
            url = url % self.show_id
            print(url, '详情页')
            res = requests.get(url, headers=self.headers)
            show_id = res.headers.get('REQUEST_ID')
            if not show_id:
                pass

            print('--' * 80)
            sleep(5)
            print(res.text)
            break


if __name__ == '__main__':
    obj = Lagou()




