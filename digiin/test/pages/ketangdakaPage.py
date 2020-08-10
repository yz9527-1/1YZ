# coding = utf-8
from digiin.test.common.start_app import Android_driver

d = Android_driver()

class KetangdakaPage():
    """签到界面"""
    def qiandao_back_element(self):

        """签到-返回按钮"""
        return d.find_element_by_xpath("//*[@text='返回']")
        """点击签到"""
        """签到按钮"""
        """签到记录"""
        """签到记录-返回按钮"""
        """在线帮助图标"""
        """在线帮助-返回"""