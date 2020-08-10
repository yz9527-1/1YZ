#encoding=utf-8

from appium import webdriver

import time
def  Android_driver():
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '5',  # 手机安卓版本
        'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
        'appPackage': 'com.dw.project.dianming',  # 启动APP Package名称
        'appActivity': 'com.dw.project.dianming.activity.SplashActivity',  # 启动Activity名称
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://192.168.0.24:4723/wd/hub', desired_caps)
    time.sleep(5)
    return driver
