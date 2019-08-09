from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '16981700'
API_KEY = 'cHLC0p7dsOUVA0idSWQxV0lf'
SECRET_KEY = 'VZCXoeuHfViaAA2EThwIHLukAYcT0pf9'

nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

if __name__ == '__main__':
    res = nlp_client.simnet('今天天气怎么样', '今天天气不好').get('score')
    print(res)
