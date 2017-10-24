'''
Created on 2017年10月23日

@author: Administrator
'''
import xlrd

xlsurl=r"Request_test_data.xlsx" #表格文件路径
filexls_obj=xlrd.open_workbook(xlsurl) #获取文件对象

sheetName=filexls_obj.sheet_names()[0]#获取表格第一个sheet的名称
sheet_obj=filexls_obj.sheet_by_name(sheetName)#获取第一个sheet的对象

total_rows=sheet_obj.nrows #获取表格总行数
total_cols=sheet_obj.ncols #获取表格总列数

cols_data=sheet_obj.col_values(0) #获取表格第一列的数据
rows_data=sheet_obj.row_values(1) #获取表格第二行的数据

print("=========================================")
print("total_rows:",total_rows)
print("total_cols:",total_cols)

print(cols_data)
print(rows_data)


