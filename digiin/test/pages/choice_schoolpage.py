# coding = utf-8
import os
import time
from appium import webdriver
import digiin.data.startdata
from digiin.test.common.start_app import Android_driver


d = Android_driver()

class Choice_SchoolPage(object):
    """请选择学校界面"""


    def qiehuanhuaijing_element(self):
        """切换测试（生产）环境"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_ChooseSchool_switch']")

    def inputshool_element(self):
        """请输入学校名称"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/et_ChooseSchool_MsgSearch']")

    def shool_element(self):
        """具体学校如：中山火炬职业技术学院"""
        return d.find_element_by_xpath("//*[@text='中山火炬职业技术学院']")

    def choice_school(self):
        """选择学校操作"""
        huanjing = self.qiehuanhuaijing_element().text
        if huanjing == "切换到生产环境":
            self.inputshool_element().click()
            self.inputshool_element().send_keys("中山火炬")
            self.shool_element().click()
        else:
            self.qiehuanhuaijing_element().click()
            self.inputshool_element().click()
            self.inputshool_element().send_keys("中山火炬")
            self.shool_element().click()


