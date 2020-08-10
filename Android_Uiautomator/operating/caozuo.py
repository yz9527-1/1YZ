#encoding=utf-8

from Android_Uiautomator.dirver.Dirver import Android_driver

d = Android_driver()
def xiahua():
        # 下滑
        d.get_window_size()
        d.swipe(start_x=500, start_y=2000, end_x=500, end_y=500, duration=300)

def shanghua():
    pass