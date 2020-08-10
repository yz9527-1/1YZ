# coding = utf-8
from digiin.test.pages.choice_schoolpage import Choice_SchoolPage
from appium import webdriver
import digiin.data.startdata
import os
from digiin.test.common.start_app import Android_driver

# d = Android_driver()
# d.implicitly_wait(5)
# Choice_SchoolPage().choice_school()



d = Android_driver()
d.implicitly_wait(5)

class LoginPage(Choice_SchoolPage):
    """登录页面"""

    def back_button_element(self):
        """返回按钮"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming: id / tv_PublicTitle_back']")

    def user_element(self):
        """请输入学号"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_account']")

    def clear_button_element(self):
        """清空按钮"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_clean']")

    def checkbox_element(self):
        """服务协议和隐私政策勾选框"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/iv_login_isAgree']")

    def login_button_element(self):
        """登录按钮"""
        return d.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/bt_login_login']")

    def cancel_button_element(self):
        """请确认个人信息弹框，取消按钮"""
        return d.find_element_by_xpath("//*[@resource-id='android:id/button2']")

    def determine_button_element(self):
        """请确认个人信息弹框，确定按钮"""
        return d.find_element_by_xpath("//*[@resource-id='android:id/button1']")
    def user_error1_element(self):
        """请输入学号"""
        pass

    def user_error2_element(self):
        """用户不存在"""
        pass

    def user_error3_element(self):
        """硬件已被xxx绑定"""
        pass

    def login(self,user):
        """登录操作"""
        if user == None:
            """先点击输入框，直接输入user"""
            self.user_element().click()
            self.user_element().send_keys(user)
        else:
            """先点击输入框，再清空输入框，再输入user"""
            self.user_element().click()
            self.user_element().clear()
            self.user_element().send_keys(user)

        state = self.checkbox_element().is_selected()
        if state == True:
            """如果已勾选，直接点击登录按钮"""
            self.login_button_element().click()
            self.determine_button_element().click()
        else:
            """如果未勾选，先点击勾选框，再点击登录按钮"""
            self.checkbox_element().click()
            self.login_button_element().click()
            self.determine_button_element().click()


