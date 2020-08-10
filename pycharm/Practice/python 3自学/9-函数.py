"""
def maxTwo(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def maxThree(x, y, z):
    if x > y:
        maxTwo(x, z)
    else:
        maxTwo(y, z)


maxThree(12, 8, 45)

import random
def custom_str(length, type):
    if type == 'number':
        s = '1234567890'
    elif type == 'letter':
        s = 'abcdrfg'
    else:
        s = '123456789asdfghjklzxcvbnm'
    return random.sample(s,length)
#测试代码
print(custom_str(6,'number'))
print(custom_str(7,'letter'))

"""
#import  string,random
#user=''.join(random.sample(string.digits,8))
#print(user)