#encoding=utf-8

import pandas as pd
import numpy as np
import pymssql


def excel(row, col):
    df = pd.read_excel('D:/PycharmProjects/Android_Uiautomator/data/data.xls')
    data = pd.DataFrame(df)
    return data.iloc[row, col]

# def csv(row, col):
#     df = pd.read_csv('D:/PycharmProjects/Uiautomator/data/data.csv')
#     data = pd.DataFrame(df)
#     print(df)
    #return data
#print(csv(0,2))

# def ssql():
#     serverName = '192.168.0.223'
#     userName = 'sa'
#     passWord = 'digiin.123'
#     connect = pymssql.connect(serverName, userName, passWord, 'PhoneSign')