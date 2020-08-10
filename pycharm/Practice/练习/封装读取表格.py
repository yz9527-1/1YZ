import xlrd

#创建工具类，操作Excel表格
class OperationExcel:
    def __init__(self,filename):
        """
         初始化类，每次传入文件名
         fielname：文件路径+文件名
        :param filename: 
        """
        self.table=xlrd.open_workbook(filename)
    def get_data_by_index(self,index=0):
        """
        通过索引读取数据
        ：index：索引
        :param index: 
        :return: 
        """

        sheet=self.table.sheet_by_index(index)
        keys=sheet.row_values(0)  #将表格的第一行作为字典的键
        rows=sheet.nrows   #获取表中的总行数
        data_list=[]
        for row in range(1,rows):
            values=sheet.row_values(row)  #逐行读取数据
            tmp=zip(keys,values)
            data_list.append(dict(tmp))
        return data_list

if __name__=='__main__':
    oper=OperationExcel("shuju.xlsx")
    data=oper.get_data_by_index()
    print(data)