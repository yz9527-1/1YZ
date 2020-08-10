# coding=utf-8
import unittest
from appium import webdriver
import digiin.data.startdata
import time
from digiin.common import swipe

driver = webdriver.Remote(digiin.data.startdata.url, digiin.data.startdata.desired_caps)
driver.implicitly_wait(5)
class Testchoice_school(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #连接Appium Server，初始化自动化环境
        print("测试开始")
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        driver.quit()

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
         print("----")
    def test_01(self):
        driver.find_element_by_xpath("//*[@text='请选择学校']").click()
        title = driver.find_element_by_xpath("//*[@text='请选择学校']").text
        assert title =="请选择学校"
        print("用例01测试成功")

    def test_02(self):
        driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_ChooseSchool_switch']").click()
        assert driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_ChooseSchool_switch']").text == "切换到测试环境"
        print("用例02测试成功")

    def test_03(self):
        driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_ChooseSchool_switch']").click()
        assert driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_ChooseSchool_switch']").text == "切换到生产环境"
        print("用例03测试成功")

    def test_04(self):
        # 点击中山火炬职业技术学院
        driver.find_element_by_xpath("//*[@text='请输入学校名称']").click()
        driver.find_element_by_xpath("//*[@text='请输入学校名称']").send_keys("中山火炬")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='中山火炬职业技术学院']").click()
        assert driver.find_element_by_xpath("//*[@text='登录']").text=='登录'
        print("用例04测试成功")


if __name__=="__main__":
    unittest.main()

