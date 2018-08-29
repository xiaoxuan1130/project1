# coding:utf-8

import xlrd
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        self.keys=self.table.row_values(1)
        self.rowNum=self.table.nrows
        self.colNum=self.table.ncols

    def dict_data(self):
        if(self.rowNum<=1):
            print("总数小于1")
        else:
            j=2
            r=[]
            for i in range(self.rowNum-2):
                s={}
                values=self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
        return r

if __name__ == '__main__':
    filepath="D:\software\收费录入数据导入模板 (1).xlsx"
    filepath=unicode(filepath, "utf-8")
    sheetName="Export"
    data=ExcelUtil(filepath,sheetName)
    print(data.dict_data())