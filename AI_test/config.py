# 静态文件配置
MUSIC_PATH = 'Musics'
COVER_PATH = 'Covers'
QRCODE_PATH = 'QRcode'
CHAT_PATH = 'Chats'

# 数据库配置
from pymongo import MongoClient

MG = MongoClient('localhost', 27017)
mongo = MG['Angel']


# Redis 配置
from redis import Redis

RDB = Redis(host='127.0.0.1', port=6379)


# 返回配置
RET = {
    "CODE": 0,
    "MSG": "",
    "DATA": {}
}

# 二维码生成API
QRCODE_URL = 'http://qr.liantu.com/api.php?text=%s'

