from pymysql import connect, cursors
from pymysql.err import OperationalError
from pymysql import escape_string
import os
import time
import json
import configparser as cparser
from commom.logger import Logger
# ===============读取db_config.ini文件设置============
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# base_dir = base_dir.replace('\\','/') #多余本身/
file_path = base_dir + "/config/db_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")

logger = Logger(logger='DB').getlog()
# =====================封装MySql操作============================


class DB:
    def __init__(self):
        try:
           # 连接数据库
            logger.info("====init data====")
            logger.info("连接数据库")
            self.conn = connect(host=host,user=user,password=password,db=db,charset='utf8mb4',cursorclass=cursors.DictCursor)
        except OperationalError as e:
            # print("Mysql Error %d: %s" % (e.args[0],e.args[1]))
            logger.info("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self, table_name):
        logger.info("清除表数据")
        real_sql = "truncate " + table_name + ";"
        # real_sql = 'delete from' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据

    def insert(self, table_name,table_data):
        logger.info("插入表数据")
        for key in table_data:
            table_data[key] = "'" +str(table_data[key]) +"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        # print(key)
        # print(value)
        # value = escape_string(value)
        real_sql = "INSERT INTO " + table_name + "("+key+")" + " VALUES " + "(" + value + ")"
        # print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库连接
    def close(self):
        logger.info("关闭数据库连接")
        self.conn.close()
        logger.info('======init data finished!=====')

    def init_data(self, datas):
        '''初始化数据'''
        logger.info("初始化数据库")
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

    def begin_data(self):
        logger.info("开始数据处理")
        self.db = DB()
        with open(os.path.dirname(os.path.dirname(__file__)) +'/config/data.json', 'r', encoding='utf8') as f:
            datas = json.load(f)
            self.db.init_data(datas)


if __name__ == '__main__':
    # db = DB()

    # table_name = "sign_event"
    # data = {'id':12,'name':'荣耀','`limit`':250,'status':1,'address':'火车南站','start_time':'2019-08-10 15:46:43'}
    # db.clear(table_name)
    # db.insert(table_name,data)
    # db.close()

    # with open('../config/data.json','r',encoding='utf8') as f:
    # 	datas=json.load(f)
    # 	db.init_data(datas)
    DB().begin_data()
