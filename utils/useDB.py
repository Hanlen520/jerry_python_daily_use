# -*- coding: utf-8 -*-
from utils import config
class mysqlDB(object):

    def __init__(self):
        return

    def connect(self):
        # change root password to yours:
        import mysql.connector
        conn = mysql.connector.connect(host=config.db_host, port=config.db_port, user=config.db_user, password=config.db_password, database=config.database,
                              auth_plugin='mysql_native_password')
        return conn

    def search(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        cursor.close()
        conn.close()
        return values

    def insert(self, sql):
        print(sql)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        try:
            conn.commit()
        except :
            print('commit error')
        conn.close()

    # 测试查询，防止sql注入
    def searchsql(self, sql, args):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        values = cursor.fetchall()
        cursor.close()
        return values

