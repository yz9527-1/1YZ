#coding=utf-8
import  sys
import  logging
import pymssql

from  _collections_abc import  Iterable

class MSSQL(object):

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd  = pwd
        self.db   = db


    def GetCnet(self):

        if not self.db:
            raise (NameError,"没有设置数据库信息")
        self.connect=pymssql.connect(host=self.host,user=self.user,pwd=self.pwd,dabatase=self.db,charset='utf8')
        cur=self.connect.cursor()
        if not cur:
            raise (NameError,'链接数据库失败')
        else:
            return  cur

    def ExcQuery(self,sql):
        """
        执行查询语句
        """
        cur=self.GetConnet()              #获取
        cur.execute(sql)                 ##执行sql语句
        resList=cur.fetchall()           ##fetchall()函数,它的返回值是多个元组,即返回多个行记录,如果没有结果,返回的是()
        self.connect.close()
        return resList


    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        :param sql: sql语句
        :return: 
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.connect.commit()
        self.connect.close()

    def test(self):
        """

        :rtype: 
        """
        from  _collections_abc import Iterable
        ms = MSSQL(host="192.168.0.223",user="sa",pwd="digiin.123",db='PhoneSign')
        resList =ms.ExcQuery("select stb_id,stb_classtime,stb_afterclasstime  from [PhoneSign].[dbo].[p_scantaskbind] where stb_classtime BETWEEN '2020-06-01 09:25:00.000' AND '2020-06-01 16:45:00.000';")

        for x in resList:

            print(x[0],x[1])

    if __name__=='__main__':
        test()
