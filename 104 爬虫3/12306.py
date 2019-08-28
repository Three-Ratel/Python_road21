import requests

session = requests.Session()
url = 'https://kyfw.12306.cn/otn/resources/login.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

page_txt = session.get(url, headers=headers).text
with open('12306.html', 'w', encoding='utf-8') as f:
    f.write(page_txt)
print('done')


params = {
    'login_site': 'E',
    'module': 'login',
    'rand': 'sjrand',
    '1566984613670': '',
    'callback': 'jQuery19107880399259875137_1566984596165',
    '_': '1566984596166'
}
url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'
code_12306 = requests.get(url, headers=headers, params=params).content
with open('code_12306.jpg', 'wb') as f:
    f.write(code_12306)
print('code_12306 done')
