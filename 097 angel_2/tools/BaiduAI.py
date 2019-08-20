import os
from uuid import uuid4

from bson import ObjectId

from config import AI_CLIENT, VOICE, CHAT_PATH, mongo
from tools.Tuling import run


def text2audio(str, filename):
    res = AI_CLIENT.synthesis(str, 'zh', 1, VOICE)
    if not isinstance(res, dict):
        audio_path = os.path.join(CHAT_PATH, filename)
        with open(audio_path, 'wb') as f:
            f.write(res)
    else:
        print(res)
    return filename


# from aip import AipSpeech
#
# """ 你的 APPID AK SK """
# APP_ID = '16981700'
# API_KEY = 'cHLC0p7dsOUVA0idSWQxV0lf'
# SECRET_KEY = 'VZCXoeuHfViaAA2EThwIHLukAYcT0pf9'
#
# AI_CLIENT = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#
# VOICE = {
#     'vol': 5,
#     'spd': 5,
#     'pit': 6,
#     'per': 4,
# }


def audio2text(filepath):
    filepath = os.path.join(CHAT_PATH, filepath)

    # 读取文件
    def get_file_content(filepath):
        os.system(f'ffmpeg -i {filepath} -f s16le -ar 16000 -ac 1 -acodec pcm_s16le  -y {filepath}.pcm')
        # os.remove(filepath)
        with open(f'{filepath}.pcm', 'rb') as fp:
            return fp.read()

    # 识别本地文件
    ret = AI_CLIENT.asr(get_file_content(filepath), 'pcm', 16000, {
        'dev_pid': 1536,
    })
    try:
        res = ret.get('result')[0]
    except:
        pass
    return res


def dispose_reco(toy_id):
    Q = audio2text('blob.wav')
    # 播放音乐
    if '我想听' in Q or '我要听' in Q or '播放' in Q:
        content_list = list(mongo.content.find({}))
        for content in content_list:
            if content.get('title') in Q:
                return {"from_user": "ai", "music": content.get('music')}

    # 主动发起聊天
    if '发消息' in Q or '聊天' in Q:
        toy = mongo.toys.find_one({'_id': ObjectId(toy_id)})
        for friend in toy.get('friend_list'):
            if friend.get('friend_remark') in Q or friend.get('friend_nick') in Q:
                filename = text2audio(f'现在可以给{friend.get("friend_remark")}聊天了', filename=f'{uuid4()}.mp3')
                return {
                    "from_user": friend.get('friend_id'),
                    "chat": filename,
                    "friend_type": 'app'
                }
    # robot接口
    answer = run(Q)
    filename = text2audio(answer, filename=f'{uuid4()}.mpp3')
    return {
        "from_user": "ai",
        "chat": filename
    }
