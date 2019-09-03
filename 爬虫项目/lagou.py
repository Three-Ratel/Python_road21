import requests

URL = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python',
}
res = requests.post(url=URL, headers=headers)
print(res.text)
