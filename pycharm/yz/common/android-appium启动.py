#coding=utf-8

from appium import webdriver


desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '10'

desired_caps['deviceName'] = 'Android Emulator'

desired_caps['appPackage'] = 'com.dw.project.dianming'

desired_caps['appActivity'] = 'com.dj.module.app.login.ui.activity.ChooseSchoolActivity'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.quit()
