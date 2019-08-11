# AI常用词汇

1.  ASR(automatic speech recongition)：语音识别
2.  TTS：text to speech：语音合成
3.  IR：image recogition：图像识别
4.  NLP：natrural language processing
5.  QPS：query per second 每秒钟允许的请求的次数

护照：世界统一格式

## 1. 语音识别

1.  需要的语音文件为 pcm，wav，amr格式，可以使用 ffmpeg 进行格式转换
2.  pycharm环境变量只在启动加载一次
3.  修改读取文件的函数：os.system的命令

```python
# 执行系统命令
import os, subprocess
res = os.system('ls')
# 0表示成功，1表示失败
print(res)
res = subprocess.Popen('ls')
os.system('xx.mp3')
os.system('ffplay xx.mp3')
```

-   相似度：60%以上就认为是相同的

```python
# 问答机器人-图灵机器人
www.tuling123.com
```

-   request使用get，post发送请求

```python
import requests
res = requests.get('url')
# content为bytes类型，text为utf8文本
print(res.content)
print(res.text)
print(res.json())

res = reqeusts.post(url, json={'k':'v'})
res.json()
```

```python
# 使用ffmpeg进行格式转换
ffmpeg -i test.mp3 -f s16le -ar 16000 -ac 1 -acodec pcm_s16le pcm16k.pcm
```









