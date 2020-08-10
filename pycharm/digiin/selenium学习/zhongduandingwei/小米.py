# coding=utf-8

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5',
    'deviceName': 'xxx',
    'appPackage': 'com.app.digiin.project.sdkdemo',
    'appActivity': 'com.app.digiin.project.sdkdemo.MainActivity',
    'unicodeKeyboard': True, 'resetKeyboard': True, 'noReset': True, 'newCommandTimeout': 6000,
                'automationName': 'UiAutomator2'}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://192.168.11.9:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)

driver.find_element_by_xpath("//*[@text='终端扫描']").click()

driver.find_element_by_xpath("//*[@resource-id='com.app.digiin.project.sdkdemo:id/accountEditTxt']").click()
driver.find_element_by_xpath("//*[@resource-id='com.app.digiin.project.sdkdemo:id/accountEditTxt']").clear()
driver.find_element_by_xpath("//*[@resource-id='com.app.digiin.project.sdkdemo:id/accountEditTxt']").send_keys("2020052804")

for i in range(1,10000):
    driver.find_element_by_xpath("//*[@text='蓝牙扫描']").click()
    print(i)
    time.sleep(15)
