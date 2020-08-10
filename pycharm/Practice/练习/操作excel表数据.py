from selenium import webdriver
import xlrd

# data=[
#     {"user":"诸葛亮1","password":"test123456"},
#     {"user":"诸葛亮2","password":"test123456"},
#     {"user":"诸葛亮3","password":"test123456"}, 
#     {"user":"诸葛亮4","password":"test123456"}
# ]
# for i in data:
#     print(i)
#     login(i["username",i["password"])  #需要先封装一个登陆login（）
#1.打开表格文件
table=xlrd.open_workbook("shuju.xlsx")
print(table)

#2.选择具体一张表
sheet=table.sheet_by_index(0)  #通过索引读取具体表格
# sheet1=table.sheet_by_name("Sheet1")  #通过表名读取具体表格
#
# print("通过索引读取",sheet)
# print("通过表名读取",sheet1)

#3.读取表中的数据
#3.1读取行  sheet.row_values(行号)行号从0开始   列表格式
row_values=sheet.row_values(0)
print(row_values)
#3.2读取列 sheet.col_values(列号)列号从0开始     列表格式
col_values=sheet.col_values(0)
print(col_values)

#3.3读取单元格sheet.cell_value(行号,列号)  具体对应单元格数据类型
cell_values=sheet.cell_value(0,1)
print(cell_values)

#3.4获取行数
print("行数：",sheet.nrows)
#3.5获取列数
print("列数",sheet.ncols)