import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):
        """
        指定保存文件的文件路径，日志级别，以及调用文件
        将日志存入到指定文件中
        :param loger:
        """
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler,用于写入日志文件
        rq = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        log_path = os.path.dirname(os.path.dirname(__file__))+'/logs/' # 项目根目录下/Logs 保存日志
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_name = log_path+rq+'.log'
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)


        #再创建一个logger，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        # fornatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fornatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fh.setFormatter(fornatter)
        ch.setFormatter(fornatter)

        #给logger添加hander
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger


