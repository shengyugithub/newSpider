import pymysql
MYSQL_DB = 'house'
MYSQL_USER = 'root'
MYSQL_PASS = '123456'
MYSQL_HOST = 'localhost'

connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,
                             password=MYSQL_PASS, db=MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass= pymysql.cursors.DictCursor)


