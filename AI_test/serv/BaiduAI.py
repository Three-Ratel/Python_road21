import os
from uuid import uuid4

import requests
from bson import ObjectId

from settings import AI_CLIENT, VOICE, CHAT_PATH, mongo, DATA, TU_SERVER_URL


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


def text2audio(str, filename):
    res = AI_CLIENT.synthesis(str, 'zh', 1, VOICE)
    if not isinstance(res, dict):
        audio_path = os.path.join(CHAT_PATH, filename)
        with open(audio_path, 'wb') as f:
            f.write(res)
    else:
        print(res)
    return filename


if __name__ == '__main__':
    # 生成语音文件
    text2audio('消息发送成功', 'SendOK.mp3')


def audio2text(filepath):
    filepath = os.path.join(CHAT_PATH, filepath)

    # 读取文件
    def get_file_content(filepath):
        os.system(f'ffmpeg -i {filepath} -f s16le -ar 16000 -ac 1 -acodec pcm_s16le  -y {filepath}.pcm')
        with open(f'{filepath}.pcm', 'rb') as fp:
            return fp.read()

    # 识别本地文件
    ret = AI_CLIENT.asr(get_file_content(filepath), 'pcm', 16000, {'dev_pid': 1536, })
    try:
        res = ret.get('result')[0]
        return res
    except:
        return '网络中断，请您重新发送语音指令'


def dispose_reco(toy_id):
    Q = audio2text('blob.wav')
    # robot接口
    DATA['perception']['inputText']['text'] = Q
    DATA['userInfo']['userId'] = toy_id
    answer = requests.post(TU_SERVER_URL, json=DATA).json().get('results')[0].get('values').get('text')
    print('语音指令为：', answer)
    # 合成 answer 语音信息
    filename = text2audio(answer, filename=f'{uuid4()}.mpp3')
    return {
        "from_user": "ai",
        "chat": filename
    }
