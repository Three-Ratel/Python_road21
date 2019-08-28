#!/usr/bin/env python
# coding:utf-8

from hashlib import md5

import requests
from lxml import etree


class VerfiedCode(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def run(file_path, style: int):
    chaojiying = VerfiedCode('bobo328410948', 'bobo328410948', '899435')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(file_path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, style)['pic_str'])  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return chaojiying.PostPic(im, style)['pic_str']


url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

get_login = requests.get(url, headers=headers).text
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(get_login)

tree = etree.HTML(get_login)
__VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
code_url = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
session = requests.Session()
get_code = session.get(code_url, headers=headers).content
with open('./files/code.jpg', 'wb') as f:
    f.write(get_code)
print('done')


data = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': '958976577@qq.com',
    'pwd': '123456',
    'code': run(f'./files/code.jpg', 1004),
    'denglu': '登录',
}

page = session.post(url, headers=headers, data=data).text
with open('success.html', 'w', encoding='utf-8') as f:
    f.write(page)
print('login done')