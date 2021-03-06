# coding=utf-8
import re,os
import time,datetime

# 读取日志文件
with open("E:\\1LYZ\\log\\monkeylog\\error20202020072704.txt","r") as file1:
    content = file1.readlines()


# 准备日志分析报告
with open("E:\\1LYZ\\monkey\\monkey_report2.txt","a") as file2:
    starttime = datetime.datetime.now()
    file2.write("now:"+str(starttime)+'\n')
    print(u'开始时间',starttime)

# 分析日志文件中的问题
    str1 = '.*ANR.*'
    str2 = '.*CRASH.*'
    str3 = '.*Exception.*'
    str4 = '.*finished.*'
    Acount,Ccount,Ecount = 0,0,0

# 遍历日志中的每一行，来查找无响应/崩溃/异常
    for i in content:
        if re.match(str1,i):
            print(u'测试过程中出现程序无响应，具体内容为：\n',i)
            file2.write(i)
            Acount += 1
        elif re.match(str2,i):
            print(u'测试过程中出现程序崩溃，具体内容为：\n',i)
            file2.write(i)
            Ccount += 1
        elif re.match(str3,i):
            print(u'测试过程中出现程序异常，异体内容为：\n',i)
            file2.write(i)
            Ecount += 1
# 如果存在任何异常则不用判断日志是否正常完成
    if Acount or Ccount or Ecount ==0:
        for i in content:
            if re.match(str4,i):
                print(u'测试过程中正常')
            file2.write(i)


    endtime = datetime.datetime.now()
    print(u'结束时间：',endtime)
    file2.write("now:"+str(endtime)+'\n')
    sumtime = (endtime - starttime).seconds
# 提示报告内容
    print(u'报告已完成，请查看分析：')
    print(u'位置：','E:\\1LYZ\\monkey\\monkey_report.txt')
    print(u'用时：',sumtime,'s')
