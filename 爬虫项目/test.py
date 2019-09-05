from requests import Session
session = Session()

headers = {
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

session.get('https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC', headers=headers)
data = {
    'first': True,
    'pn': '1',
    'kd': 'Python',
}
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false'
res = session.post(url=url, data=data, headers=headers).json()
print(res, type(res))