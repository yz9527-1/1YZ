
# coding = utf-8

from appium import webdriver
import time


def Android_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5',
        'deviceName': 'xxx',
        'appPackage': 'com.dw.project.dianming',
        'appActivity': 'com.dw.project.dianming.activity.SplashActivity',
        'unicodeKeyboard': True, 'resetKeyboard': True, 'noReset': False, 'newCommandTimeout': 6000,
                    'automationName': 'UiAutomator2'}

# 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://192.168.11.9:4723/wd/hub', desired_caps)
    time.sleep(5)
    return driver