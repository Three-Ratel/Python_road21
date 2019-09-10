#### 1. 简述cookie的概念和作用 

-   cookie概念：由服务器产生，浏览器收到响应后，存储在浏览器本地的一组组健值对
-   作用：解决http协议无状态的问题

#### 2. 简述scrapy各个核心组件之间的工作流程

1.  引擎：进行数据流的处理、触发事物，负责控制系统所有组件的数据流
2.  调度器：用于接收引擎发过来的请求，并在引擎再次请求的时候返回，对reqest对象去重
3.  下载器：基于twisted高效异步模型
4.  爬虫：开发人员自定义的类，用于爬取网页和解析数据
5.  项目管道：包括数据清理、验证、持久化

#### 3. 基于crwalSpider实现数据爬取的流程

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

#### 4. 在scrapy中如何实现将同一份数据值存储到不同的数据库中

1.  使用基于管道的持久化存储
2.  item对象首先传递给第一个优先级最高的管道类
3.  优先级最高的管道类处理完数据后，传递给下个一个管道类
4.  每个管道类需要return item传递给下一个管道类

#### 5. scrapy的下载中间件的作用以及类中重点方法的使用介绍

1.  可以对请求对象添加 UA 代理和 ip代理
2.  process_request(self, request, response, spider)
    -   主要是对请求进行处理，更改请求头
3.  process_repose(self, request, response, spider)
    -   可以对异常的响应进行处理，返回原来的request对象，会重新跳读下载



#### 6.  scrapy的pipeline的作用及其工作原理

1.  用于持久化存储
2.  通过yield关键字进行交给scrapy优先级最高的管道类

#### 7. 有关scrapy的pipeline中的process_item方法的返回值有什么注意事项

1.  如果有多个管道类需要对item进行操作，需要return item 给下一个管道类
2.  如果只有一个管道类可以不使用返回值

#### 8. scrapy实现持久化存储有几种方式，如何实现  

1.  基于终端的持久化存储

    ```python
    scrapy crawl 爬虫文件 -o data.csv
    ```

2.  基于管道的

    ```python
    1. 数据解析好后
    2. 打开item类并定义相关属性，把数据存储到item中
    3. 向管道提交item，
    4. 在管道文件中的 process_item 方法中进行持久化存储
    5. 在settings.py 中开启管道类
    ```

#### 9. 描述使用xpath实现数据解析的流程

1.  导入模块：from lxml import xpath
2.  实例化得到 etree对象，tree = etree.HTML(response)/etree.parse(xxx.html)
3.  数据解析：tree.xpath('xpath表达式')

#### 1. 你如何处理相关动态加载的页面数据

1.  方案一：可以使用 selenium 进行动态页面的爬取，进行数据解析
2.  方案二：
    -   在开发者工具中查找动态数据来源
    -   确定请求发送的方式
    -   手动发送请求，获取需要的数据

#### 11. 如何实现分布式？简述其实现和部署流程

1.  使用 scrapy + scrapy-radis组件实现
2.  构造链接提取器和规则解释器
    -   实例化一个 Rule() 的对象
    -   实例化链接提取器，LinkExtractor(allow=r'正则表达式', callback=parse，follow=True)
    -   callback：进行数据解析

#### 12. 谈谈你对https数据加密方式的理解

1.  证书密钥加密方式ssl
2.  非对称密钥加密
3.  证书密钥加密

#### 13. 原生的scrapy框架为什么不可以实现分布式？

1.  原生的scrapy没有共享的管道
2.  没有共享的调度器

#### 14. 常见的反爬机制有哪些？如何进行处理？  

1.  robots协议：忽略
2.  UA检测：添加user-agent
3.  ip检测：使用ip代理
4.  动态参数：一般在原来的页面
5.  伪标签：提取自定义的属性名
6.  cookies：使用request.session()
7.  验证码：selenium + 打码平台(如：超级鹰)
8.  js混淆：js反混淆
9.  reffer请求来源检测：添加请求来源

#### 15. 在爬虫中如何实现数据清洗（三种清洗方法）

-   df是DataForm对象

1.  df.drop(labels=[df.isnull().all(axis=0).index], axis=0)
2.  df.dropna(axis=0)
3.  df.fillna(axis=0)











