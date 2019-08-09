from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16981700'
API_KEY = 'cHLC0p7dsOUVA0idSWQxV0lf'
SECRET_KEY = 'VZCXoeuHfViaAA2EThwIHLukAYcT0pf9'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('床前明月光，疑是地上霜。举头望明月，低头思故乡。', 'zh', 1, {
    'vol': 5,
    'spd': 6,
    'pit': 6,
    'per': 4,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)

else:
    print(result)
