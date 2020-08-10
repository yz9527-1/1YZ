from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
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

# driver.find_element_by_id('com.dw.project.dianming:id/et_ChooseSchool_MsgSearch').click()
# driver.find_element_by_id('com.dw.project.dianming:id/et_ChooseSchool_MsgSearch').send_keys('中山火炬')
# driver.find_element_by_id("com.dw.project.dianming:id/tv_schoolname_item").click()
#
# driver.find_element_by_id('com.dw.project.dianming:id/ed_login_account').clear()
# driver.find_element_by_id('com.dw.project.dianming:id/ed_login_account').send_keys('2020052807')
#
# driver.find_element_by_id('com.dw.project.dianming:id/bt_login_login').click()
#
# driver.find_element_by_id('android:id/button1').click()


driver.find_element_by_id('com.dw.project.dianming:id/ll_homeRecycleView_secondary').click()

for i in range(50000):
    print(i)


    try:
        #driver.swipe(start_x=500, start_y=500, end_x=500, end_y=1000, duration=300)
        #time.sleep(2)

        if driver.find_element_by_id('com.dw.project.dianming:id/tv_homeClassSign_sign_sign').text=="签到":
            driver.find_element_by_id('com.dw.project.dianming:id/tv_homeClassSign_sign_sign').click()
            time.sleep(30)
            print("签到成功")
            print("-------------------")
        else:
            print("签到失败")
            print("-------------------")
            time.sleep(30)
            continue
    except :
        print("发生异常，重新打开app")
        driver = webdriver.Remote('http://192.168.11.9:4723/wd/hub', desired_caps)
        driver.implicitly_wait(30)
        driver.find_element_by_id('com.dw.project.dianming:id/ll_homeRecycleView_secondary').click()
        continue


else:
    print("操作已完成")





#driver.find_element_by_id('com.dw.project.dianming:id/iv_homeClassSign_sign_circle').click()
# driver.close()