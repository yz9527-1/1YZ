from appium import webdriver
import digiin.data.startdata
import time
driver = webdriver.Remote(digiin.data.startdata.url, digiin.data.startdata.desired_caps)


# 获取机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0]*0.5)       # x坐标
    y1 = int(l[1]*0.75)      # 起始y坐标
    y2 = int(l[1]*0.25)      # 终点y坐标
    print(x1)
    print(y1)
    print(y2)
    driver.swipe(x1,y1,x1,y2,t)

# 屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)     # x坐标
    y1 = int(l[1] * 0.35)     # 起始y坐标
    y2 = int(l[1] * 0.85)     # 终点y坐标
    print(x1)
    print(y1)
    print(y2)
    driver.swipe(x1, y1, x1, y2, t)

# 屏幕向左滑动
def swipeLeft(t):
    l = getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
# 屏幕向右滑动
def swipeRight(t):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,t)

# time.sleep(3)
# l = getSize()
# print(l)
# time.sleep(3)
# swipeUp(1000)
# print('向上滑动')
#
# time.sleep(3)
# swipeLeft(1000)
# print('向左滑动')
#
# time.sleep(3)
# swipeRight(1000)
# print('向右滑动')
#
# time.sleep(3)
#
# swipeDown(1000)
# print('向下滑动')
#
# print('结束')
