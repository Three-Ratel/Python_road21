from multiprocessing import JoinableQueue
from threading import Thread

import requests
from bs4 import BeautifulSoup

"""爬取三国演义所有章节"""
url = 'http://www.purepen.com/sgyy/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
}

page_text = requests.get(url, headers=headers).text
page_text = page_text.encode('iso-8859-1').decode('gbk')
# print(page_text)
soup = BeautifulSoup(page_text, 'lxml')
info = soup.find('table', cellpadding=3)
title_list = info.select('tr>td')


def common():
    count = 0
    fp = open('./files/sanguo.txt', 'w', encoding='utf')
    for i in title_list[1::2]:
        content_url = url + i.a['href']
        chapter = title_list[count].string.strip() + ' ' + i.a.string
        count += 2
        content = requests.get(content_url, headers=headers).text
        try:
            content_text = content.encode('iso-8859-1').decode('gbk')
            content_text = content_text.encode('utf8').decode('utf8')
        except:
            content_text = content.encode('iso-8859-1').decode('utf8')

        soup = BeautifulSoup(content_text, 'lxml')
        content = soup.find('pre').string
        fp.write(chapter + content + '\n')
        fp.flush()

    fp.close()


"""线程版"""


def get_url(jq):
    count = 0
    for i in title_list[1::2]:
        content_url = url + i.a['href']
        chapter = title_list[count].string.strip() + ':' + i.a.string
        count += 2
        content = requests.get(content_url, headers=headers).text
        try:
            content_text = content.encode('iso-8859-1').decode('gbk')
            content_text = content_text.encode('utf8').decode('utf8')
        except:
            continue

        soup = BeautifulSoup(content_text, 'lxml')
        content = soup.find('pre').string
        jq.put([chapter, content])
    jq.join()
    return True


def wirte_content(jq):
    while True:
        info = jq.get()
        if not info: continue
        chapter = info[0]
        content = info[1]
        file_name = chapter.split(':')[0].replace(' ', '')
        print(file_name)
        with open(f'./files/threadings/{file_name}.txt', 'w', encoding='utf8') as fp:
            fp.write(chapter + content + '\n')
        jq.task_done()


if __name__ == '__main__':

    jq = JoinableQueue()
    for i in range(5):
        tp = Thread(target=get_url, args=(jq,))
        tp.start()
    for i in range(10):
        tp = Thread(target=wirte_content, args=(jq,))
        tp.daemon = True
        tp.start()
