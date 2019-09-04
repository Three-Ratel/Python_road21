## 1. 基于Crwalspider的全站爬取

-   Crawlspider是Spider的子类

### 1.1 使用流程

1.  创建一个项目和基于Crawlspider的爬虫文件
    -   `scrapy startproject projectName`
    -   `scrapy genspider -t crawl spiderName www.xx.com`
2.  构造链接提取器和规则解释器
    1.  实例化一个Rule()的对象：规则解析器
    2.  LinkExtractor()：链接提取器(**可以根据指定的规则，进行链接的提取**)
        -   提取的规则：allow='正则表达式'如：`r'type=4&page=\d+'`,局部正则即可
    3.  规则解析器：用作数据解析
        -   获取链接提取器提取的链接，对其进行请求发送，根据**指定规则(callback)**对请求到的页面源码数据进行数据解析
        -   follow=True：表 用下次访问页面时也要进行链接的提取
            -   将链接提取器继续作用到链接提取器提取的页码链接中
    4.  链接提取器和规则解析器也是一一对应的

### 1.2 爬虫文件示例

```python
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunsiteItem

class SunSpider(CrawlSpider):
    name = 'sun'
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    link = LinkExtractor(allow=r'question/\d+/\d+.shtml')
    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), callback='parse_item', follow=True),
        Rule(link, callback='parse_detail'),
    )

    def parse_item(self, response):
        item = {}
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            url = tr.xpath('./td[2]/a[2]/@href').extract_first()
            # print(title, url)
        yield item

    def parse_detail(self, response):
        num = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        title = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[1]/text()').extract_first()
        print(num)
        item = SunsiteItem()
        item['num'] = num
        item['title'] = title
        yield item
```

## 2. 分布式

### 1. 概念

-   分布式爬虫：基于多台电脑组件一个分布式机群，然后让机群中的每一台电脑执行同一组程序，然后对同一个网站数据进行分布爬取
-   目的：提取爬取数据的效率(环境搭建较为复杂)
-   爬取静态数据

### 2. 实现

#### 1. 实现分布式方式

1.  基于celery
2.  基于scrapy+radis实现：scrapy结合scrapy-radis组件实现的分布式
    -   原生的scrapy无法实现分布式
        -   调度器不能共享造成request对象重复
        -   管道不能共享
3.  scrapy-radis作用
    -   提供可以被共享的调度器和管道

#### 2. 基于scrapy框架和scrapy-radis

1.  安装scrapy-radis：pip install scrapy-redis
2.  创建一个工程和spider文件(需要修改spider文件)
    -   导入包：`from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider`
    -   将当前爬虫父类修改为`RedisCrawlSpider`
    -   redis_key = 'fbsQueue'：表示共享的队列名称，替换start_urls
3.  settings.py
    1.  开启共享管道
        -   `ITEM_PIPELINES = {'scrapy_redis.pipelines.RedisPipeline': 400}`
    2.  共享调度器
        -   `DUPEFILTER_CLASS='scrapy_redis.dupefilter.RFPDupeFilter'`：过滤器类
        -   `SCHEDULER=`'scrapy_redis.scheduler.Scheduler'：调度器
        -   `SCHEDULER_PERSIST = True`：实现增量式
    3.  指定redis的服务
        -   REDIS_HOST='ip地址'
        -   REDIS_PORT=6379
4.  修改redis的配置文件：redis.conf
    1.  默认绑定关掉
    2.  protected-mode no
    3.  携带配置文件启动redis：`./redis-server /etc/myredis.conf`
5.  启动当前工程：
    -   进入爬虫对应的目录中：`scarpy runspider fbs.py`
    -   队列在redis中：lpush fbsQueue '**起始的url**'
        -   lrang fbs:items 0 -1：查询数据
        -   flushall：清空数据
        -   llen fbs:item

-   配置文件：settings.py

```python
# 开启共享管道
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
# 指定使用可被共享的调度器
# 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# 使用scrapy-redis组件自己的调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
SCHEDULER_PERSIST = True

# 指定redis，ip 和 端口
REDIS_HOST = '192.168.11.25'
REDIS_PORT = 6379
```

## 3. 增量式爬虫

### 1. 简介

1.  概念：监测网站数据更新情况。
2.  核心：去重
3.  对应两种不同的增量式网站
4.  深度爬取类型的网站需要对详情页的url进行记录和检测
    -   **记录**：将爬取过的详情页的url进行记录保存(**redis 中的set中**)
    -   **检测**：如果对某一个详情页的url发起请求之前先要记录表中进行查看，该url是否存在，存在的话认为这个url已经爬取了

### 2. 数据库操作

```python
# redis的set集合
127.0.0.1:6379> keys *
(empty list or set)
127.0.0.1:6379> sadd name henry
(integer) 1
127.0.0.1:6379> sadd name echo
(integer) 1
127.0.0.1:6379> sadd name henry
(integer) 0
127.0.0.1:6379> smembers name
1) "echo"
2) "henry"
127.0.0.1:6379> 
```

### 3. 深度爬取示例

-   深度爬取的url需要持久化存储，通过redis插入的返回值确认当前url是否被爬取

```python
import scrapy
from redis import Redis
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZlspcItem

class MoviesSpider(CrawlSpider):
    name = 'movies'
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/id/5/page/1.html']
    rules = (
        Rule(LinkExtractor(allow=r'vod/show/id/5/page/\d+.html'), callback='parse_item', follow=True),)
    conn = Redis(host='localhost', port=6379)
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/div/h4/a/text()').extract_first()
            url = 'https://www.4567tv.tv/' + li.xpath('./div/a/@href').extract_first()
            item = ZlspcItem()
            item['title'] = title
            if self.conn.sadd('url', url):
                yield scrapy.Request(url=url, callback=self.parse_detail, meta={'item': item})
            print('当前%s数据已经获取...' % url)

    def parse_detail(self, response):
        item = response.meta['item']
        detail = response.xpath('/html/body/div[1]/div/div/div/div[2]/p//text()').extract()
        detail = ''.join(detail)
        item['detail'] = detail
        yield item
```

-   非深度爬取类型的网站

    -   名词：数据指纹
    -   如果没有url进行判断可以使用内容进行摘要生成数据指纹，进而通过上述方法进行判断

    









