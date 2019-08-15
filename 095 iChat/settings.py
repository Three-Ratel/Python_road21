# 目录相关配置
AVATAR = 'iAvatar'
RECORD = 'iRecord'


#
from pymongo import MongoClient

MG = MongoClient('127.0.0.1', 27017)

mongo = MG['ichat']

# 返回协议
RET = {
    'code': 0,
    'msg': '',

}
