
# coding = utf-8
from digiin.test.common.start_app import Android_driver

d = Android_driver()
class HomePage():
    """首页界面"""

    """点点课堂"""
    def ketangdaka(self):
        """课堂打卡"""
        return d.find_element_by_xpath("//*[@text='课堂打卡']")

    def lishiqiandao(self):
        """历史签到"""
        return d.find_element_by_xpath("//*[@text='历史签到']")

    def kechengbiao(self):
        """课程表"""
        return d.find_element_by_xpath("//*[@text='课程表']")


    """点点宿舍"""
    def kaoqinglishi(self):
        """历史考勤"""
        return d.find_element_by_xpath("//*[@text='考勤历史']")

    def erweimakaimen(self):
        """二维码开门"""
        return d.find_element_by_xpath("//*[@text='二维码开门']")

    def sushekaoqing(self):
        """宿舍考勤"""
        return d.find_element_by_xpath("//*[@text='宿舍考勤']")

    """成绩查询"""
    def yingyusiliuji(self):
        """英语四六级"""
        return d.find_element_by_xpath("//*[@text='英语四六级']")

    def jisuanjidengji(self):
        """计算机等级"""
        return d.find_element_by_xpath("//*[@text='计算机等级']")

    def putonghuakaozheng(self):
        """普通话考级"""
        return d.find_element_by_xpath("//*[@text='普通话考级']")


    """点点健康"""
    def wugancewen(self):
        """无感测温"""
        return d.find_element_by_xpath("//*[@text='无感测温']")

    def jiankangwenjuan(self):
        """健康问卷"""
        return d.find_element_by_xpath("//*[@text='健康问卷']")

    def jiankangma(self):
        """健康指南"""
        return d.find_element_by_xpath("//*[@text='健康指南']")

    """点点校园"""
    def xiaoyuantongzhi(self):
        """校园通知"""
        return d.find_element_by_xpath("//*[@text='校园通知']")

    def tupianshangchuan(self):
        """图片上传"""
        return d.find_element_by_xpath("//*[@text='图片上传']")

    def my_button(self):
        """我的按钮"""
        return d.find_element_by_xpath("//*[@text='我的']")