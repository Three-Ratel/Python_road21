import datetime
from random import random

import pymysql
from gevent import monkey
from lxml import etree
from redis import Redis
from requests import Session

monkey.patch_all()
host = '192.168.43.246'
conn = pymysql.connect(host=host, user='triclub', password="123", database='TriClub')
cur = conn.cursor()
my_redis = Redis(host='localhost', port=6379)


class Lagou(object):
    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'www.lagou.com',
        'Upgrade-Insecure - Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',

    }
    data = {
        'first': True,
        'pn': '1',
        'kd': 'Python',
    }
    urls = []

    def __init__(self, page, proxies, city):
        self.session = Session()
        self.item = {}
        # page表示爬取的页码
        self.page = page
        # proxies表示使用的代理
        self.proxies = proxies
        self.city = city

    def get_session(self):
        self.session.get(f'https://www.lagou.com/jobs/list_Python?px=default&city={self.city}',
                         headers=self.headers, proxies=self.proxies)

    def get_first_page(self):
        self.data['pn'] = f'{self.page}'
        url = f'https://www.lagou.com/jobs/positionAjax.json?px=default&city={self.city}&needAddtionalResult=false'
        response = self.session.post(url=url, data=self.data, headers=self.headers, proxies=self.proxies).json()
        print(response)
        '公司名称、公司地址、公司类型领域、岗位名称、python方向、薪资、学历、经验、职位描述、任职要求、公司规模'
        company_list = response['content']['positionResult']['result']
        for company_dict in company_list:
            try:
                self.item['company_name'] = company_dict['companyFullName']
                self.item['city'] = company_dict['city']
                self.item['field'] = company_dict.get('industryField')
                self.item['position_name'] = company_dict.get('positionName')
                self.item['direction'] = company_dict.get('secondType')
                self.item['salary'] = int(company_dict.get('salary').replace('-', '').split('k')[0])
                self.item['education'] = company_dict.get('education')
                self.item['work_year'] = company_dict.get('workYear')
                self.item['district'] = company_dict.get('district')
                self.item['company_size'] = company_dict.get('companySize')
                position_id = company_dict.get('positionId')
                url = f'https://www.lagou.com/jobs/{position_id}.html'
                print(self.item)
                # self.urls.append(url)
            except:
                pass
            self.get_detial_page(url)
        print(f'第{self.page}页数据获取完毕')

    def get_detial_page(self, url):
        print(url, '详情页')
        if my_redis.sadd('url', url):
            self.set_cookies()
            res = self.session.get(url, headers=self.header, proxies=self.proxies)
            tree = etree.HTML(res.text)
            detail_info = ''.join(tree.xpath('//*[@id="job_detail"]/dd[2]/div//text()'))
            detail_info.replace(' ', '').replace('.', '')
            self.item['detail_info'] = detail_info
            address_lis = tree.xpath('//*[@id="job_detail"]/dd[3]/div[1]//text()')
            address = ''.join(address_lis[:-2]).replace(' ', '').replace('\n', '')
            self.item['address'] = address
            gevent.spawn(self.write(self.item))
            gevent.sleep(random() * 3)
            print(url, 'done')
        else:
            print(f'{url}数据已获取')

    def set_cookies(self):
        user_trace_token = self.session.cookies.get('user_trace_token')
        strtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        user_trace_token = strtime + user_trace_token[14:]
        '20190907210715-d9dfb911-07bb-4d91-82d3-03fd4d203860'
        del self.session.cookies['user_trace_token']
        self.session.cookies.set('user_trace_token', user_trace_token)

    def write(self, item):
        try:
            item = item.copy()
            company_name = item['company_name']
            field = item['field']
            position_name = item['position_name']
            direction = item['direction']
            salary = item['salary']
            education = item['education']
            work_year = item['work_year']
            district = item['district']
            address = item['address']
            company_size = item['company_size']
            detail_info = item['detail_info']
            city = item['city']
            print(item)
            try:
                cur.execute(
                    """insert into lagou_triclub(companyName,city,district,address,companyfield,positionname,pythondirection,salary,education,workyear,positiondesc,requiremnents,companysize) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")""" % (
                        company_name, city, district, address, field, position_name, direction,
                        salary, education, work_year, detail_info, "null", company_size))
                conn.commit()
            except:
                pass
        except:
            pass


def run(page, proxies, city):
    obj = Lagou(page, proxies, city)
    obj.get_session()
    obj.get_first_page()


import gevent


# url = 'http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=2&fa=0&fetch_key=&groupid=0&qty=50&time=1&pro=&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=2'
# response = requests.get(url)
# tree = etree.HTML(response.text)
# url_list = tree.xpath('//body//text()')

# 代理池
# proxy_pool = []
# if not proxy_pool:
#     for url in url_list:
#         dic = {'https': url}
#         proxy_pool.append(dic)


def lagou(city):
    g_l = []
    index = 0
    for i in range(1, 500):
        # if proxy_pool and index == len(proxy_pool) - 1:
        #     index = 0
        #     proxy = proxy_pool[index]
        #     print(proxy, i)
        try:
            # 不使用代理
            proxy = {}
            g = gevent.spawn(run(i, proxy, city))
            g_l.append(g)
        except Exception as e:
            # proxy_pool.pop(index)
            tip = f'第{i}页爬取失败\n'
            print(tip)
            with open('error.log', 'a', encoding='utf-8') as f:
                f.write(tip)
            print(e)
        index += 1
        print('-' * 8)

    gevent.joinall(g_l)


if __name__ == '__main__':
    lagou(city='上海')
