#encoding=utf-8

from HTMLTestRunner import HTMLTestRunner
import os
import unittest
import time


CasePath = "D:\PycharmProjects\Android_Uiautomator\operating"
ReportPath = "D:\PycharmProjects\Android_Uiautomator"
# 用例路径
case_path = os.path.join(CasePath)
# 报告存放路径
report_path = os.path.join(ReportPath, 'report')
# print(report_path)
def all_case():
    # 执行test开头的py文件
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    return discover
if __name__ == '__main__':
    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(report_path, "result" + now + ".html")

    # 打开一个文件，将result写入此file中
    fp = open(report_abspath, 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title=u"自动化测试报告",
                                           description=u"用例执行详情:")
    runner.run(all_case())
    fp.close()