#coding=utf-8
import os
import time
import datetime
print(time.ctime())
print(time.time())
print(datetime.datetime.now())


print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(os.getcwd())
print(os.listdir())