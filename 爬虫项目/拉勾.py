import json
import time

# from pymongo import MongoClient
from requests import Session

# mongo = MongoClient('127.0.0.1', 27017)
# MC = mongo['lagou']
session = Session()

headers = {
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

response_2 = session.get('https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC', headers=headers)
data = {
    'first': True,
    'pn': '1',
    'kd': 'Python',
}

time.sleep(5)
response = session.post(
    'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false',
    data=data, headers=headers).json()

# print(response, type(response))

for i in range(2, 31):
    print(i)
    for dic in response['content']['positionResult']['result']:
        RET = {}
        peo_dic = response['content']['hrInfoMap'].pop(str(dic['positionId']))
        dic.update(peo_dic)
        dic.pop('companyShortName')
        RET[dic['companyFullName']] = json.dumps(dic)
        # MC.work.insert_one(RET)
    data = {
        'first': False,
        'pn': str(i),
        'kd': 'Python',
        'sid': response['content']['showId']
    }
    time.sleep(2)
    response = session.post(
        'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false',
        data=data, headers=headers).json()
