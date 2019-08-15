# 静态文件配置
MUSIC_PATH = 'Musics'
COVER_PATH = 'Covers'

# 数据库配置
from pymongo import MongoClient

MG = MongoClient('localhost', 27017)
mongo = MG['Angel']

# 返回配置
RET = {
    "CODE": 0,
    "MSG": "",
    "DATA": {}
}
