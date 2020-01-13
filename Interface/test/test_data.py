import json
import unittest
import os,time
import warnings
from HTMLTestRunner import HTMLTestRunner
import ddt
# from jiekou.common.common import SL_EQ
from Interface.read_excel.read_excel import ExcelUtil
from Interface.request_case.casedemo import SET
from db_fixtrue.mysql_db import DB
from commom.logger import Logger
from Interface.test.data_get import DA
excel = ExcelUtil(r"F:\Project\python\Interfect_framework\case\guest1.xlsx", "工作表1")
logger=Logger(logger='DataTest').getlog()
@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        DB().begin_data()
        logger.info("接口测试开始")
        # print('接口测试开始...')
    @classmethod
    def tearDownClass(cls):
        logger.info("接口测试结束")
        # print('...接口测试结束')
#         #遍历获取列表的数据#
    @ddt.data(*excel.next())
    def test01(self,data):
        logger.info("处理用例数据")
        #每次遍历后将字典置为空
        # data1 = {}
        url = data['接口地址']
        method=data['请求方式']
        test_data = data['参数']
        Except=data['预期结果']
        case=data['断言方式']
        rquest_data=DA().get_data(test_data)

        if method == 'get':
            result=SET().test_get1(url)
        elif method == 'get1':
            result=SET().test_get1(url,rquest_data)
        elif method == 'post':
            # data2 = json.dumps(test_data)
            logger.info('POST请求')
            result=SET().test_ppp(url,rquest_data)
        elif method == 'put':
            result=SET().test_put1(url,rquest_data)
        # print(result)
        if  case=="assertIn":
            logger.info('断言assertIn')
            self.assertIn(Except,result)
        if  case=="assertEqual":
            logger.info('断言assertEqual')
            self.assertEqual(result,Except)
        if case == "test_post":
            self.assertEqual(Exception,result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
	# 设置报告文件保存路径
    report_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/report/'

    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 设置报告名称格式
    HtmlFile = report_path + now + "HTMLTemplate.html"
    # fp = open(HtmlFile, 'wb')

    with open(HtmlFile,'wb+') as f:
	    HTMLTestRunner(stream=f, title="XX项目测试报告", description="用例执行情况").run(suite)






