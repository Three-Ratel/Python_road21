import os

from aip import AipSpeech

from similiar import nlp_client
from robot import run
""" 你的 APPID AK SK """
APP_ID = '16981700'
API_KEY = 'cHLC0p7dsOUVA0idSWQxV0lf'
SECRET_KEY = 'VZCXoeuHfViaAA2EThwIHLukAYcT0pf9'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    os.system(f'ffmpeg -i {filePath} -f s16le -ar 16000 -ac 1 -acodec pcm_s16le {filePath}.pcm')
    with open(f'{filePath}.pcm', 'rb') as fp:
        return fp.read()


# 识别本地文件
res = client.asr(get_file_content(f'audio.mp3'), 'pcm', 16000, {
    'dev_pid': 1536,
})

query = res.get('result')[0]

if nlp_client.simnet(query, '今天天气怎么样？').get('score') >= 0.6:
    A = '今天有雷阵雨'
else:
    A = run(txt=query)
result = client.synthesis(A, 'zh', 1, {
    'vol': 5,
    'spd': 4,
    'pit': 6,
    'per': 4,
})


# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('answer.mp3', 'wb') as f:
        f.write(result)
    os.system(f'ffplay answer.mp3')
else:
    print(result)
