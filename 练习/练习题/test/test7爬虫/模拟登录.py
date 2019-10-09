# from time import sleep
#
# from selenium import webdriver
#
# bro = webdriver.Chrome(executable_path='/Users/henry/Downloads/Tools/chromedriver')
# url = 'https://github.com/login'
#
# bro.get(url)
# username = bro.find_element_by_xpath('//*[@id="login_field"]')
# password = bro.find_element_by_xpath('//*[@id="password"]')
# sign_in = bro.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[7]')
#
# username.send_keys('Henry-wzh')
# password.send_keys('xxxxxxx')
# sign_in.click()
# sleep(3)
#
# page_text = bro.page_source
# with open('login_main.htm', 'w', encoding='utf-8') as f:
#     f.write(page_text)
#
# bro.quit()
import time

from lxml import etree
from requests import Session

session = Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
url = 'https://github.com/login'
page = session.get(url, headers=headers)
time.sleep(3)
tree = etree.HTML(page.text)
login_url = 'https://github.com/session'

data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'login': 'Henry-wzh',
    'password': 'xxxxx',
    'webauthn-support': 'supported',
    'required_field_5d35': '',
}

timestamp = tree.xpath('//*[@id="login"]/form/div[3]/input[5]/@value')
timestamp_secret = tree.xpath('//*[@id="login"]/form/div[3]/input[6]/@value')
authenticity_token = tree.xpath('//*[@id="login"]/form/input[2]/@value')
data['timestamp'] = timestamp
data['timestamp_secret'] = timestamp_secret
data['authenticity_token'] = authenticity_token

res = session.post(login_url, data=data, headers=headers)
time.sleep(3)
with open('login_main.htm', 'w', encoding='utf-8') as f:
    f.write(res.text)
print(res.text)
