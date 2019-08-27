# 数据库配置
# mongodb
from pymongo import MongoClient

MG = MongoClient('127.0.0.1', 27017)
mongo = MG['AI_test']

# redis
from redis import Redis

redis_cli = Redis(host='127.0.0.1', port=6379, db=6)

# 配置头像存储目录
ICON_PATH = 'icon'
CHAT_PATH = 'chat/rec'


# 百度ai
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16981700'
API_KEY = 'cHLC0p7dsOUVA0idSWQxV0lf'
SECRET_KEY = 'VZCXoeuHfViaAA2EThwIHLukAYcT0pf9'

AI_CLIENT = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

VOICE = {
    'vol': 5,
    'spd': 5,
    'pit': 6,
    'per': 4,
}


# 图灵机器人
TU_SERVER_URL = 'http://openapi.tuling123.com/openapi/api/v2'
DATA = {

    "perception": {
        "inputText": {
            "text": "附近的酒店"
        }
    },

    "userInfo": {
        "apiKey": "2213889293634c759484cac88a91c170",
        "userId": "110"
    }
}
