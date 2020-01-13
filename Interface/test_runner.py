import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner

from Interface.test.test_data import DataTest
# from db_fixtrue.mysql_db import DB
suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
# 设置报告文件保存路径

report_path = os.path.dirname(os.path.dirname(__file__)) + '/report/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLTemplate.html"
# fp = open(HtmlFile, 'wb')


if __name__ == '__main__':
    # DB().begin_data()
    with open(HtmlFile, 'wb+') as f:
        HTMLTestRunner(
            stream=f,
            title="XX项目测试报告",
            description="用例执行情况").run(suite)
