import os, json
def ls():
    user_home = os.listdir('/Users/henry/programme/python/Python_codes/projects/2.tcp_upload_download')
    user_home = json.dumps(user_home).encode('utf-8')
    print(user_home)
ls()