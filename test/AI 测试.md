### /1. 简述智能玩具项目背景 2

1.  目的：为了增进亲子关系，通过我们的智能玩具打通父母和孩子之间的沟通壁垒
2.  提出智能玩具项目的是我的合伙人老李，他有两个孩子（一个男孩3岁和女孩5岁）他常年在北京工作通常每年只能见到子女一次，由于常年和子女沟通很少，与孩子的关系日渐疏远，这个问题一直困扰着老李，后来想到了制作一个智能玩具，一方面是孩子的玩具，另一方面是他与孩子沟通的纽带。
3.  项目由此应运而生，我们主要负责提供软件开发，公司的硬件部负责开发硬件。
4.  成型：我们使用的是獭兔包皮和环保填充物（出于对孩子的保护和让父母放心）

### 2. 项目应用技术以及技术实现功能 5

1.  Flask：提供业务逻辑

2.  WebSocket：提供实时推送消息的通信服务

3.  MongoDB：提供存储用户数据、内容等，后期进行用户画像

4.  Redis：存储效率速度快，用来存储热点数据，如用户未读消息条数

5.  BaiduAI接口：ASR、TTS，语音识别和语音合成（文本相似度处理）

6.  联图接口：根据设备唯一识别符，生成二维码，为添加、绑定玩具使用

7.  图灵机器人：用于toy端的语音指令识别

8.  mui：用于开发前端页面

9.  plus：用于调用硬件资源如：摄像头、录音机

10.  requests：用于内容数据采集

     

### 3. 产品功能简述 5

#### app:

-   用户注册和登录
-   绑定玩具、添加玩具为好友、控制玩具好友列表
-   获取内容数据
-   推送幼教内容给玩具
-   与toy进行通信

#### toy:

-   接收语音、歌曲
-   toy间通信，接收未读消息
-   主动发起聊天

#### 后台:

-   主要是提供业务逻辑相关的接口

```python
# flask提供服务
/content_list				# 获取资源内容
/get_cover/filename			# 获取cover
/get_music/filename			# 获取music
/reg						# 注册成功后返回login页面
/login						# 登录，返回除password外的 user 信息
/auto_login					# index页面请求，返回除password外的 user 信息
/scan_qr					# 对toy的uuid进行校验，不合法、未绑定、已绑定
/bind_toy					# 通过app绑定toy，并建立两者的关系
/toy_list					# 获取app绑定的所有toy
/friend_list				# 获取朋友列表
/chat_list					# 获取历史聊天记录
/app_uploader				# app 发送语音消息
/toy_uploader 				# toy 发送语音消息
/recv_msg					# toy 接收语音消息
/ai_uploader				# 处理 toy 的语音指令、对接图灵机器人
/add_req					# 添加好友请求
/add_req					# 添加好友请求
/ref_req					# 拒绝好友请求
/acc_req					# 接受好友请求
```

### 4. Flask 中的 Response 及作用 5

1.  '' ：直接返回字符串
2.  render_template：返回html页面
3.  redirect()：重定向
4.  send_file()：发送文件流
5.  jsonify()：返回 json 格式内容

### 5. 回答以下属性的作用 5

request.args：存储url中参数

request.form：存储form/formdata中的数据m

request.files：存储文件信息

request.data：请求头没有form/formdata，没有时，存储原始文件数据

request.json：请求头中application/json，存储请求体中数据

### 6. before_request 和 after_request 的正常和异常执行顺序 3

-   before_request：在view函数执行之前
-   after_request：在view函数执行之后
-   errorhandler()：异常时执行

正常：执行完before_request之后，执行view函数，执行所有的after_request

异常：执行view异常时，执行errorhander()，之后执行所有的after_request()

### 7.简述 Flask 路由中 endpoint 和 methods 的作用 2

-   endpoint：flask用于添加路由使用
-   methods：指定请求方式

### 8. MongoDB中的增删改查方法 3 

1.  updateOne，updateMany

    -   $set修改器，用于修改旧属性，增加新属性

    -   $unset：删除属性
    -   $inc：增加值

2.  insert：增加

    -   insertOne({key:value})
    -   insertMany({})

3.  remove：删除

    -   remove({})

4.  find，findMany()



### 7.  使用文档

1.  /register：用户注册，可以上传头像，不上传默认 icon.jpg
2.  /login：用户登录，登录后跳转聊天窗口
3.  /get_icon：获取头像接口
4.  /web_chat/<user_id>：通过user_id获取个人聊天窗口
    -   可以单聊和群聊
5.  /friend_list：获取所有好友列表，在线人数
    -   通过点击好友，可以进行私聊
6.  /get_img：获取好友头像