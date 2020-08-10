# coding=utf-8
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'xxx',
    'appPackage': 'com.dw.project.dianming',
    'appActivity': 'com.dw.project.dianming.activity.SplashActivity',
    'unicodeKeyboard': True, 'resetKeyboard': True, 'noReset': True, 'newCommandTimeout': 6000,
                'automationName': 'UiAutomator2'}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://192.168.11.9:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)

#界面1
#点击手机屏幕
driver.find_element_by_xpath("//*[@text='请选择学校']").click()
#页面互动到最底部
time.sleep(5)
driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=500, duration=300)
time.sleep(3)
print('滑动成功')
#点击中山火炬职业技术学院
driver.find_element_by_xpath("//*[@text='中山火炬职业技术学院']").click()

#界面2
a=driver.find_element_by_xpath("//*[@resource-id='com.dw.project.dianming:id/ed_login_account']")
a.click()
a.clear()
a.send_keys('2020052806')

toast_message='手机硬件已被*'
driver.find_element_by_xpath("//*[@text='登录']").click()
message ='//*[@text=\'{}\']'.format(toast_message)

# 获取toast提示框内容
toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element)
#print(toast_element.text)

#driver.find_element_by_xpath("//*[@resource-id='android:id/button1']").click()

# driver.find_element_by_id('com.dw.project.dianming:id/ll_homeRecycleView_secondary').click()
#
#
# driver.find_element_by_id('com.dw.project.dianming:id/tv_homeClassSign_sign_sign').click()
#
# toast_message = "本次签到已提交，请稍后查看签到结果"
# message ='//*[@text=\'{}\']'.format(toast_message)
#
# # 获取toast提示框内容
# toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
# print(toast_element)
# print(toast_element.text)
# assert toast_element.text == toast_message
# print('断言成功')