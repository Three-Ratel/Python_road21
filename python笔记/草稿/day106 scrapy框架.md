## 1. 移动端数据爬取

-   基于某一款抓包工具：fillder、Charles(青花瓷)、miteproxy

### 1. fillder使用流程

1.  fillder配置：tools -->  options --> connection --> allow remote ...
2.  `http://fillder所在pc的 ip+port/：访问到提供证书下载的页面`
3.  fiddler所在的pc设备和手机在同一网段下，手机端进行访问下载，并且信任
4.  配置手机代理配置成fiddler所在pc机的ip和fillder的端口
5.  fiddler就可以捕获到手机的http/https请求

```python

```

## 2. scrapy框架

### 1. 环境准备

1.  常用的爬虫框架：pyspider、scrapy
    -   框架：就是一个集成了各种功能且具有很强通用性(可以应用到各种不同的需求中)的项目模版。
    -   学习框架中封装好的相关功能的使用。
    -   一般发送get请求
2.  scrape：集成的功能
    -   高性能的数据解析操作、持久化存储、高性能的数据下载操作
    -   Twisted：实现异步功能，scrapy的异步功能依赖

### 2. 使用

1.  创建一个工程：scrapy startproject firstBlood
2.  spiders：爬虫包，`__init__.py`，爬虫文件位置
    1.  创建爬虫文件：scrapy genspider 爬虫文件名 url
    2.  name：爬虫文件名称(唯一)
    3.  allowed_domains=['url'] 允许的域名
    4.  start_urls = [url1, url2...] ；通常是网站的首页
3.  settings：当前工程配置文件
    1.  user-agent
    2.  不遵循robots协议
    3.  LOG_LEVEL = 'ERROR'

#### Note

1.  xpath返回的仍然是 list 类型，但数据内容被scrapy 进行了封装
2.  在scrapy中，xpath中的 text() 返回的不是 string类型，而是selector对象
3.  text() 获取的数据在该**对象**中/**list 中的对象**中(**scrapy封装的数据解析方式**)
    -   selector对象使用 .extract() 方法取出数据data
    -   selector对象的list 也可以使用 .extract() 方法循环取出数据(list类型)
    -   .extract_first()：列表中的第一个数据进行提取

```python
# 终端使用
cd 项目名称
scrapy genspider 爬虫文件名 url
# 无日志输出，如果有错误则以日志形式输出
scrapy crawl 爬虫文件名 --nolog
# 设置log_level='error',解决报错输出问题
```

-   爬虫文件：qiubai.py

```python
import scrapy
from ..items import QiubaiItem

class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/hot/', ]

    def parse(self, response):
        div_list = response.xpath('///*[@id="content-left"]/div')
        for div in div_list:
            author = div.xpath('./div/a/h2/text()').extract_first()
            content = div.xpath('./a/div/span//text()').extract()
            print(author)
            print(content)
            item = QiubaiItem()
            item['author'] = author
            item['content'] = content
            yield item
```

-   items.py

```python
import scrapy
class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    content = scrapy.Field()
```

-   pipelines.py

```python
class QiubaiPipeline(object):

    fp = None
    def open_spider(self):
        print('开始爬虫')
        self.fp = open('qiubai.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content)
        return item

    def close(self):
        print('结束爬虫')
        self.fp.close()
```

### 3. 持久化存储

#### 1. 基于终端

-   特性：只可以将parse方法的返回值存储到本地磁盘的文件中
-   只支持：'json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle'

```python
# 执行 qiubai.py 文件并存储到quibai.csv
scrapy crawl qiubai	-o qiubai.csv
```

#### 2. 基于管道

-   实现流程
    1.  数据解析
    2.  在item类中定义相关的属性
    3.  将解析的数据存储或者封装到一个**item类型的对象中**，items文件中对应类的对象(**items实例化需要多次**即循环里)
    4.  向管道提交 item
    5.  在管道文件中的process_item方法进行持久化存储
    6.  在settings.py中开启管道
        -   ITEM_PIPELINES = {'管道类': 优先级, ...}
        -   可以设置多个管道类：数字越小优先级越高

```python
# items.py
class QiubaiItem(scrapy.Item):
	# Filed可以存储任何基本类型数据
    author = scrapy.Field()
    content = scrapy.Field()

# test.py
# 将解析的数据存储到item对象中
item = QiubaiItem()
item['author'] = author
item['content'] = content
# 提价数据到pipeline。item 被提交给优先级最高的管道类
yield item

# pipeline.py
class QiubaiPipeline(object):
    
    def open_spider(self, spider):
        fp = None
        print('开始爬虫。。。')
        slef.fp = open('quishi.txt', 'w', encoding='utf8')
    
    # 用来接收爬虫文件提交的item，并进行持久化存储
    # item就是接收的item对象
    # 每接收一个 item 就会调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+':'+content+'\n')
        # 返回下一个即将执行的管道类
        return item
    
    def close_spider(self, spider):
		print('结束爬虫')
        self.fp.close()
```

#### 3. 持久到数据库

-   将同一份数据持久化存储到不同的平台中
    1.  管道文件中的一个管道类负责数据的一种持久化存储
    2.  爬虫文向管道提交的item只会提交给优先级最高的管道类
    3.  如果使用多个管道类，需要在管道类中使用return item方法

```python
# pipeline.py 持久化到mysql。
class MysqlPL(object):
    con = None
    cursor = None

    def open_spider(self, spider):
        print('*' * 32)
        self.con = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='spider',
                                   charset='utf8')
        print(self.con)

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        sql = 'insert into qiubai values ("%s", "%s")' % (author, content)
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        return item

    def close_spider(self, spider):
        print(self.cursor, self.con)
        self.cursor.close()
        self.con.close()
```

-   持久化到redis
-   查询数据：**lrange data 0 1**

```python
class MyRedis(object):
    con = None

    def open_spider(self, spider):
        self.con = Redis(host='127.0.0.1', port=6379, db=1)
        print(self.con)

    def process_item(self, item, spider):
        # pip install -U redis==2.10.6
        self.con.lpush('data', item)
        return item
```

### 4. 手动请求发送

-   场景：爬取和解析多个页面
-   yield scrapy.Request(url, callback)
    -   页面布局不一样时，callback需要使用其他解析方法

```python
# 通用的url模版
url = ''
pageNum = 1
# parse第一调用表示的是用来解析第一页对应页面
def parse(self, response):
    。。。。
    if self.pageNum <= 5:
        self.pageNum += 1
        new_url = url % self.pageNum
        # 手动请求发送，默认是get请求，yield关键字修饰
        yield scrapy.Request(new_url, callback=self.parse)
```

-   发送POST请求

```python
data = {}				# 请求参数
url = 'xxx'				# 请求url
# 发送post请求
yield scrapy.FormRequest(url, formdata=data, callback)
```

### 5. scarpy五大核心组件工作流程

![scarpy组件](/Users/henry/Documents/截图/Py截图/scarpy组件.png)

1.  引擎(EGINE)

    -   引擎负责控制系统所有组件之间的数据流，并在某些动作发生时触发事件。有关详细信息，请参见上面的数据流部分。
    -   进行数据流的处理、触发事务(**对象的实例化、方法的调用**)

2.  **调度器(SCHEDULER)**

    -   用来接收引擎发过来的请求, 压入**队列**中, 并在引擎再次请求的时候返回. 可以想像成一个URL的优先级队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
    -   队列和过滤器

3.  **下载器(DOWLOADER)**

    -   用于下载网页内容, 并将网页内容返回给EGINE，下载器建立在**twisted这个高效的异步模型**上

4.  **爬虫(SPIDERS)**

    -   SPIDERS是开发人员自定义的类，用来解析responses，并且提取items，或者发送新的请求

5.  **项目管道(ITEM PIPLINES)**

    -   在items被提取后负责处理它们，主要包括清理、验证、持久化（比如存到数据库）等操作

6.  下载器中间件(Downloader Middlewares)

    -   位于Scrapy引擎和下载器之间，主要用来处理从EGINE传到DOWLOADER的请求request，已经从DOWNLOADER传到EGINE的响应response，你可用该中间件做以下几件事

    1.  process a request just before it is sent to the Downloader (i.e. right before Scrapy sends the request to the website);
    2.  change received response before passing it to a spider;
    3.  send a new Request instead of passing received response to a spider;
    4.  pass response to a spider without fetching a web page;
    5.  silently drop some requests.

7.  **爬虫中间件(Spider Middlewares)**

    -   位于EGINE和SPIDERS之间，主要工作是处理SPIDERS的输入（即responses）和输出（即requests）













