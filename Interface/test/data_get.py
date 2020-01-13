import json
import os

from commom.logger import Logger

logger=Logger(logger='DA').getlog()
class DA(object):


    def init_data(self, datas,test_data):
        '''初始化数据'''
        logger.info("遍历取出数据")
        global have_data
        for table, data in datas.items():
            if table == test_data:
                have_data=data
                return have_data




    def get_data(self,test_data):
        logger.info("开始获取数据")
        self.db = DA()
        with open(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/config/request.json', 'r', encoding='utf8') as f:
            datas = json.load(f)
            return  self.db.init_data(datas,test_data)