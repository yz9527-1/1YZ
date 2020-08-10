# coding=utf-8
import unittest
from appium import webdriver
import digiin.data.startdata
import time
from digiin.common import swipe

driver = webdriver.Remote(digiin.data.startdata.url, digiin.data.startdata.desired_caps)
driver.implicitly_wait(5)

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")
        driver.find_element_by_xpath("//*[@text='请输入学校名称']").click()
        driver.find_element_by_xpath("//*[@text='请输入学校名称']").send_keys("中山火炬")
        driver.find_element_by_xpath("//*[@text='中山火炬职业技术学院']").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        driver.quit()
    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        print("------")

    def test_01(self):
        driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_account']").click()
        driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_account']").clear()
        driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_account']").send_keys("2020052804")
        driver.find_element_by_xpath("//*[@text='登录']").click()
        driver.implicitly_wait(5)
        assert driver.find_element_by_xpath("//*[@text='确定']").text == "确定"
        print("用例01测试成功")

    # def text_02(self):
    #     a = driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']").is_selected()
    #     driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']").click()
    #     a1 = driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']").is_selected()
    #     print(a)
    #     print(a1)
    def test_02(self):
        driver.find_element_by_xpath("//*[@text='确定']").click()
        assert driver.find_element_by_xpath("//*[@text='中山火炬职业技术学院']").text == "中山火炬职业技术学院"
        print("用例02测试成功")


if __name__ == "__main__":
    unittest.main()

