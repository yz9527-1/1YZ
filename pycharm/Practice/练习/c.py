#encoding='utf-8'
import pymssql
from collections.abc import Iterable
import unittest

class MSSQL(object):
    '''
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启
    用法：
    '''

    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def GetConnect(self):
        '''
        得到链接信息
        :return:
        '''
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.connect=pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,charset='utf8')
        cur = self.connect.cursor()
        if not cur:
            raise (NameError, "链接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        '''
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id,NickName)
        :param sql: sql语句
        :return:
        '''
        cur=self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.connect.close()
        return resList

    def ExecNonQuery(self, sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.connect.commit()
        self.connect.close()

def test():
        from collections.abc import Iterable
        ## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
        ## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        ms = MSSQL(host="127.0.0.1",  user="sa", pwd="123", db="test")
        resList = ms.ExecQuery('SELECT * FROM abc')
        for x in resList:
            print(x[0], x[1])


if __name__ == '__main__':

    test=MSSQL('192.168.0.223','sa','digiin.123','PhoneSign')
    test.GetConnect()
    test.ExecQuery('select * from [PhoneSign].[dbo].[p_histotyrecord]')
