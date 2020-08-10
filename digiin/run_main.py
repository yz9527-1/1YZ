# coding=utf-8
import os,time,unittest,ddt,data,unpack

import HTMLTestRunner

# 获取当前路径
current_path=os.path.abspath(os.path.dirname(__file__))
report_path=current_path+'/report/'

# 获取当前时间
now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# 标题
title=u"迪进点点测试报告"

# 设置报告存放路径，并且以当前时间进行报告命名
report_abspath = os.path.join(report_path,title+now+'.html')

def all_case():
    """导入所有的用例"""
    case_path=os.getcwd()
    discover=unittest.defaultTestLoader.discover(case_path,pattern="Test*.py")

    print(discover)
    return discover



if __name__=="__main__":
    fp=open(report_abspath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=title)
    runner.run(all_case())
    fp.close()