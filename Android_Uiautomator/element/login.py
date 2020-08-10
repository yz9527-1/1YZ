#encoding=utf-8
from Android_Uiautomator.dirver.Dirver import Android_driver
import time

d = Android_driver()
#   def fanhui(self):
    #   返回
#       fanhui = self.driver.find_element_by_xpath("//*[@text='返回']")
#       return fanhui
def xiahua():
        # 下滑
    d.swipe(start_x=500, start_y=2000, end_x=500, end_y=500, duration=300)

def huoju(id, num):
        #2.学院名称：中山火炬职业技术学院
    d.find_elements_by_id(id)[num].click()


def name(id, user):
        #3.用户名输入框
        d.find_element_by_id(id).send_keys(user)

def denglu(id):
        # 8.登录
    d.find_element_by_id(id).click()

def queren(id):
        # 二次确认弹框--确认
    d.find_element_by_id(id).click()


                # def qingkong(self):
        #     #4.点击清空图标  x
        #     qingkong = self.driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_clean']")
        # #     return qingkong
        # def gouxuan(self):
        #     #5.勾选框
        #     gouxuan = self.driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']")
        #     return gouxuan
        # def xieyi(self):
        #     #6.服务协议
        #     self.driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_login_agree2']")
        # def yingsi(self):
            #7.隐私政策
        #   self.driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/tv_login_agree4']")
