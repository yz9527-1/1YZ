from selenium import webdriver
import time
import os
from appium import webdriver
import digiin.data.startdata


class BasePage(object):
    """基础页面"""

    def __init__(self,base_url = None,base_desired_caps = None):

        if base_url is None:
            self.base_url = digiin.data.startdata.url
        else:
            self.base_url = base_url

        if base_desired_caps is None:
            self.base_desired_caps = digiin.data.startdata.desired_caps
        else:
            self.base_url = base_url

    def start_up_app(self):
        driver = webdriver.Remote(digiin.data.startdata.url, digiin.data.startdata.desired_caps)
        driver.find_element_by_xpath()
    def open_page(self):
        """打开默认页面"""
        self.driver = webdriver.Remote(digiin.data.startdata.url, digiin.data.startdata.desired_caps)
        time.sleep(1)

    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面且退出程序"""
        return self.driver.quit()


d = BasePage().start_up_app()

d.find_element_by_xpath("//*[@text='课堂打卡']").clack
