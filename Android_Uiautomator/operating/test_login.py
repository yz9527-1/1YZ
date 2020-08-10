#encoding=utf-8

import uiautomator2 as u2
import os
import time
from Android_Uiautomator.element import login
from Android_Uiautomator.data import data
from Android_Uiautomator.dirver.Dirver import Android_driver
import unittest

class Login_test(unittest.TestCase):
     def setUp(self):
        pass
     def test_Login_A(self):
         login.xiahua()
         time.sleep(2)
         login.huoju(data.excel(0,1), int(data.excel(0,2)))
         time.sleep(1)
         login.name(data.excel(1,1), int(data.excel(1,3)))
         time.sleep(1)
         login.denglu(data.excel(2,1))
         time.sleep(5)
         login.queren(data.excel(3,1))
#
     def tearDown(self):
          pass
#
if __name__ == '__main__':
    unittest.main()
    # def Suite():
    #     suiteTest = unittest.TestSuite()
    #     suiteTest.addTest(Login('test_Login_A'))
    #     return suiteTest
    # runner.run(Suite())







