# coding = utf-8

from selenium.webdriver.common.by import By
import time


class TabOperation(object):
    """
    Tab操作
    """
    def __init__(self,driver):
        self.driver = driver


    def get_all_tab(self):
        """
        获取所有的tab
        """
        time.sleep(1)
        # 获取所有的tab父元素
        tab_fathers = [{'tabs1':By.CLASS_NAME,'a2':By.TAG_NAME},
                       {'tabs':By.CLASS_NAME,'a':By.TAG_NAME},]
        # 获取画面显示父元素下的所有tab
        for tab_father in tab_fathers:
            keys = list(tab_father.keys())
            values = list(tab_father.values())
            # 如果找到的父节点为空，则父节点不存在，则查找的tab不匹配
            if self.driver.find_elements(values[0],keys[0]).__len__() > 0:
                ul = self.driver.find_element(values[0],keys[0])
                tabs = ul.find_elements(values[1],keys[1])
                return tabs
    def switch_tab(self,tab_text):
        """
        切换tab
        """
        tabs = self.get_all_tab()
        for tab in tabs:
            if tab.text == tab_text:
                tab.click()
                return


if __name__ == '__main__':     from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost:35877/#/')
time.sleep(1)
tab = TabOperation(driver)
tab.switch_tab('Tab2')
# driver.quit()

