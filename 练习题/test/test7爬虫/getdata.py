import re

from requests import Session

session = Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
session.get('http://kuaixun.eastmoney.com/ssgs.html', headers=headers)

fp = open('stack.txt', 'w', encoding='utf-8')
for page in range(1, 3):
    url = f'http://newsapi.eastmoney.com/kuaixun/v1/getlist_103_ajaxResult_50_{page}_.html'
    res = session.get(url=url, headers=headers).text
    print(res)
    content = re.findall(r'"digest":"(.*?)","simdigest":', res)
    content = '//'.join(content)
    fp.write(f'第{[page]}页:{content}\n')

fp.close()

