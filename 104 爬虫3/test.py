"""使用代理ip"""
import random

import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


def test_proxy():
    url = 'https://www.baidu.com/s'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    params = {'wd': 'ip'}
    page_text = requests.get(url, params=params, headers=headers, proxies={'https': '111.231.90.122:8888'}).text
    with open(f'./files/proxy.html', 'w', encoding='utf8') as f:
        f.write(page_text)
    print('done')


# test_proxy()

"""爬取 快代理的 代理ip"""


def use_proxy():
    url = 'http://ip.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=50&time=1&pro=&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=2'
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    # print(tree.xpath('/html/body//text()'), '*' * 8)
    return tree.xpath('/html/body//text()')


def get_proxy(page):
    url = 'https://www.kuaidaili.com/free/inha/%d/' % page
    page_text = requests.get(url, headers=headers, proxies={'https': random.choice(ip_list)}).text
    tree = etree.HTML(page_text)
    tr_proxy_list = tree.xpath('//*[@id="list"]/table/tbody/tr')
    for tr in tr_proxy_list:
        ip = tr.xpath('./td[1]/text()')[0]
        port = tr.xpath('./td[2]/text()')[0]
        style = tr.xpath('./td[4]/text()')[0]
        dic = {style: f'{ip}:{port}'}
        proxy_list.append(dic)
    print(page, '页完成')


# if __name__ == '__main__':
#     from multiprocessing.dummy import Pool
#
#     ip_list = use_proxy()
#     proxy_list = []
#     pool = Pool()
#     try:
#         pool.map(get_proxy, range(1, 1001))
#     except:
#         pass
#     with open('./files/proxies.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(proxy_list))
#     print(len(proxy_list))


"""cookie 反爬"""


def cookie():
    url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json'
    params = {
        'since_id': '-1',
        'max_id': '20346182',
        'count': '15',
        'category': '-1'
    }
    session = requests.Session()
    session.get('https://xueqiu.com/', headers=headers)
    page_text = session.get(url, params=params, headers=headers).text
    print(page_text)
# cookie()





