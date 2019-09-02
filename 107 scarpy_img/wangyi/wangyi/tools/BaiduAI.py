from aip import AipNlp
import requests

""" 你的 APPID AK SK """
APP_ID = '17162320'
API_KEY = 'klOYpQdCGGooVtkDBzsEnzwo'
SECRET_KEY = 'QVI7DrG2EyNi19wAmaQ6pS2LnAHd8891'

ACESS_KEY_URL = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}'
ACESS_KEY = requests.get(ACESS_KEY_URL).json().get('access_token')
# print(ACESS_KEY)
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)




