# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class BasePage(object):
    """
    基础界面
    """
    def __init__(self,base_url = None):
        """
        基础的参数， webdriver 、默认访问的 url
        :param driver: 浏览器驱动
        :param base_url: 默认打开的 url ，一般都是登录页面
        """
        # driver = webdriver.Chrome()
        # driver.get('http://localhost:35877/#/')


        if base_url is None:
            self.base_url = 'http://localhost:35877/#/'
        else:
            self.base_url = base_url

        # 设置默认打开的页面
        self.open_page()

    def open_page(self):
        """
        打开，默认页面
        """

        self.base_url  = 'http://localhost:35877/#/'

        self.driver.maximize_window()
        self.driver.implicitly_wait()
        self.driver.get(self.base_url)
        time.sleep(1)

    def close_page(self):
        """
        关闭页面
        """
        return self.driver.close()

    def quit_driver(self):
        """
         关闭页面且退出程序
        """
        return self.driver.quit()

    def find_element(self, by, element):
        """
        返回单个定位元素
        """
        time.sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        """
         返回一组定位元素
        """
        time.sleep(1)
        return self.driver.find_elements(by, element)

    def switch_alert(self):
        """
        返回一组定位元素
         """
        time.sleep(1)
        return self.driver.switch_to.alert

    def log_out(self):
        """
        退出登录
        """
        return self.select_menu("退出登录")


