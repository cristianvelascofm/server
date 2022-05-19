from logging import root
import pymysql

def get_connection():
    return pymysql.connect(host='localhost', user='root',passwd='',db='test')
    