# coding=utf-8
import unittest
from appium import webdriver
import digiin.data.startdata
import time
from digiin.common import swipe

driver = webdriver.Remote(digiin.data.startdata.url, digiin.data.startdata.desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[@text='请输入学校名称']").click()
driver.find_element_by_xpath("//*[@text='请输入学校名称']").send_keys("中山火炬")
driver.find_element_by_xpath("//*[@text='中山火炬职业技术学院']").click()
a = driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']").is_selected()
driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']").click()
a1 = driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']").is_selected()
print(a)
print(a1)