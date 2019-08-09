import os

from aip import AipSpeech

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

print(res.get('result')[0])
