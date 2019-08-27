import requests

url = 'https://movie.douban.com/top250'
start = range(25, 250, 25)
for i in start:
    params = {
        'start': start,
        'filter': '',
    }
    headers = {
        'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    res = requests.get(url=url, params=params, headers=headers)
    print(res.text)



