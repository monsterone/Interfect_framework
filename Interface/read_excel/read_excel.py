import xlrd
from commom.logger import Logger
logger=Logger(logger='ExcelUtil').getlog()
class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        logger.info('初始化表格')
        #读取Excel对象
        self.data = xlrd.open_workbook(excelPath)
        #读取Excel表格
        self.table = self.data.sheet_by_name(sheetName)
        # get titles 获取一行或一列的值，参数是第几行
        self.row = self.table.row_values(0)
        # self.col= self.table.col_values(0)

        # get rows number 获取总行数
        self.rowNum = self.table.nrows
        # get columns number 获取总列数
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1
    def next(self):
        logger.info('读取表格数据')
        r = []
        while self.hasNext():
            s = {}
            #获取每一行的值
            col = self.table.row_values(self.curRowNo)
            #总列数
            i = self.colNum
            for x in range(i):
            #创建字典，标题为键，内容为值
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r
    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True
if __name__ == '__main__':
    excel = ExcelUtil(r"C:\Users\pc\Desktop\guest1.xlsx", '工作表1')
    data = excel.next()
    print(data)

