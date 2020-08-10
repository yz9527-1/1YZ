import pymssql
import pymssql
from collections.abc import Iterable
from collections.abc import Iterator
serverName = '192.168.0.223'
userName = 'sa'
passWord = 'digiin.123'
connect = pymssql.connect(serverName, userName, passWord, 'PhoneSign')
if connect:
    print("连接成功")

cursor=connect.cursor()
sqlvalue="select top 5 stb_id,stb_classtime,stb_afterclasstime  from [PhoneSign].[dbo].[p_scantaskbind] where stb_classtime BETWEEN '2020-06-01 09:25:00.000' AND '2020-06-01 16:45:00.000';"
try:
    cursor.execute(sqlvalue)
    result = cursor.fetchall()
    connect.commit()
    for row in result:

        stb_id=row[0]
        stb_classtime=row[1]
        stb_afterclasstime = row[2]


        print(stb_id,stb_classtime,stb_afterclasstime )
except:
    print("获取数据失败")

cursor.close()
