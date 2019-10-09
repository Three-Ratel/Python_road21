题目:Web聊天室 90分

要求:

​    使用 FlaskWeb 框架完成开发工作

​    使用 MongoDB 数据库

需求:

​    1.注册登录功能 要求 存储头像  5

​        1.注册 - 数据库 - 写入用户名密码

​        2.头像 - 上传文件 request.files - 名字保存数据

​        3.登录 - 校验用户名密码



​    2.聊天室在线人数及明细 5

​        user_socket_dict = { user1:连接 , user2:连接 , user3:连接}

​        在线人数 : len(user_socket_dict)

​        明细:  list(user_socket_dict.keys())



​    3.选择联系人实现单点对话(私聊) 10

​        websocket 单聊 复制代码



​    4.公共聊天室(群聊) 10

​        websocket 群聊 复制代码



​    5.可以发送语音消息 和 图片消息 10

​        web录音复制代码

​        发送图片 input request.files



​    6.实现聊天记录存储 和 查询 5

​        没有好友关系,就自动创建两个人的聊天对话框

​        {

​            form_user:"123",

​            chat_type:"audio"/"image"

​            message:"audio.mp3"/"image.jpg"

​        }



​    7.简述的项目功能及使用方式(项目文档,附加分值) 20

​        阐述你的项目功能 

​        说明你项目的使用方式

​    

​    8.实现Ai对话功能: 

​        语音消息Ai对话功能 10

​        文字消息Ai对话功能 10

​        功能提示 : 百度AI + 图灵机器人 





智能玩具 30分

1.简述智能玩具项目背景 2



2.项目应用技术以及技术实现功能 5



3.产品功能简述 5

app:



toy:



后台:



4.Flask 中的 Response 及作用 5



5.回答以下属性的作用 5

request.args

request.form

request.files

request.data

request.json



6.before_request 和 after_request 的正常和异常执行顺序 3



7.简述 Flask 路由中 endpoint 和 methods 的作用 2



8.MongoDB中的增删改查方法 3 