import pymysql

conn = pymysql.Connect(host='localhost', port=3306, user='root', password='root', db='news')
cursor = conn.cursor()


