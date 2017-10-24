'''
Created on 2017年10月24日

@author: Administrator
'''
import xlrd

class DataPackageTest:
    
    def xlsxSheet(self,xlsFile):
        xlsFile_obj=xlrd.open_workbook(xlsFile)
        sheetName=xlsFile_obj.sheet_names()[0] #获取第一个sheet名称
        sheet_obj=xlsFile_obj.sheet_by_name(sheetName)
        return sheet_obj


if __name__ == '__main__':
    xlsDataTest=DataPackageTest()
    fileUrl="Request_test_data.xlsx"
    
    sheetObj1=xlsDataTest.xlsxSheet(fileUrl)
    nrow=sheetObj1.nrows
    ncols=sheetObj1.ncols
    col_data=sheetObj1.col_values(0)
    row_data=sheetObj1.row_values(1)
    
    print(col_data)
    print(row_data)
    
    
    
    
    