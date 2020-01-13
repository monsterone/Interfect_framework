import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os
from Interface.test.test_data import DataTest
from commom.logger import Logger
import configparser as cparser

logger=Logger(logger='Report').logger

# ===============读取email_config.ini文件设置============
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# base_dir = base_dir.replace('\\','/') #多余本身/
file_path = base_dir + "/config/email_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path,encoding='utf-8')

mail_from = cf.get("emailconf", "mail_from")
password = cf.get("emailconf", "password")
mail_to = cf.get("emailconf", "mail_to")
title = cf.get("emailconf", "title")
connect = cf.get("emailconf", "connect")


class Report(object):

    def __init__(self):
        logger.info('初始化邮件数据')
        self.mail_from=mail_from
        self.password=password
        self.mail_to=mail_to
        self.title=title
        self.connect=connect

    #发送邮件
    def send_mail_attr(self,file_new):
        logger.info('发送邮件初始化')
        #初始化数据
        mail_from = self.mail_from
        password = self.password
        mail_to = self.mail_to
        mail_title = self.title
        connect=self.connect

        # 读取内容，相当于mail_content
        with open(file_new,'rb') as f:
            mail_content=f.read()

       #调用添加正文方法
        msg=self.email_content(mail_title,mail_content)
        #调用附件方法
        msg= self.email_attr(file_new, msg)
        #调用发送邮件
        self.email_connect(mail_from,password,mail_to,msg,connect)

    # 添加邮件内容
    def email_content(self,mail_title,mail_content):
        logger.info('添加邮件正文')
        # 添加邮件
        msg = MIMEMultipart()
        msg['Subject'] = Header(mail_title, 'utf-8')
        msg['From'] = mail_from
        msg['To'] = mail_to
        # 邮件正文内容
        msg.attach(MIMEText(mail_content,'html','utf-8'))
        return msg


    #构建附件
    def email_attr(self,file_new,msg):
        logger.info('添加邮件附件')
        # 构造附件1
        att_file = open(file_new, 'rb').read()
        att1 = MIMEText(att_file, 'base64', 'utf-8')
        att1["Conent-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment;filename="result.html"'
        msg.attach(att1)
        return msg


    #连接、发送
    def email_connect(self,mail_from,password,mail_to,msg,connect):
        logger.info('邮件服务器连接')
        smtp = smtplib.SMTP()
        smtp.connect(connect)
        smtp.login(mail_from, password)
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp.quit()
        logger.info('邮件发送成功')
        print('email has send out !')


    # 查找最新生成的测试报告
    def get_new_file(self,files):
        logger.info('查找最新生成的测试报告')
        lists = os.listdir(files)
        lists.sort(key=lambda fn: os.path.getmtime(files + "\\" + fn))
        file_ = os.path.join(files, lists[-1])
        # print(file_)
        return file_


if __name__ == '__main__':
    Report()
