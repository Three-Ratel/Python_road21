import random
import time

import gevent
import requests
from lxml import etree

"""爬取图片"""
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
}


def get_img():
    url = 'http://sc.chinaz.com/tupian/meinvtupian.html'
    _url = 'http://sc.chinaz.com/tupian/meinvtupian_%d.html'

    for i in range(1, 10):
        if i == 1:
            page_text = requests.get(url, headers=HEADERS).text
        else:
            page_text = requests.get(_url % i, headers=HEADERS).text
        tree = etree.HTML(page_text)

        data_list = tree.xpath('//div[@id="container"]/div')
        for data in data_list:
            src = data.xpath('./div/a/img/@src2')[0]
            title = data.xpath('./div/a/img/@alt')[0].encode('iso-8859-1').decode('utf8')
            img = requests.get(src, headers=HEADERS).content
            with open(f'./imgs/{title}.jpg', 'wb') as f:
                f.write(img)


def get_cv(page):
    if page == 1:
        url = 'http://sc.chinaz.com/jianli/free.html'
    else:
        url = f'http://sc.chinaz.com/jianli/free_{page}.html'
    page_text = requests.get(url, headers=HEADERS).text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@id="container"]/div')
    for div in div_list:
        href = div.xpath('./a/@href')[0]
        title = div.xpath('./a/img/@alt')[0].encode('iso-8859-1').decode('utf8')

        ppt_text = requests.get(href, headers=HEADERS).text
        tree = etree.HTML(ppt_text)
        li_list = tree.xpath('//div[@id="down"]/div[2]/ul/li/a/@href')
        rank = random.randint(0, len(li_list) - 1)
        ppt_url = li_list[rank]
        print(ppt_url, rank, page)
        ppt = requests.get(ppt_url, headers=HEADERS).content
        gevent.spawn(write, title, ppt)


def write(title, ppt):
    with open(f'./cvs/{title}{time.time()}.rar', 'wb') as f:
        f.write(ppt)


if __name__ == '__main__':
    start = time.time()
    g_l = []
    for i in range(1, 500):
        g = gevent.spawn(get_cv, i)
        g_l.append(g)
    gevent.joinall(g_l)
    print(time.time() - start)
