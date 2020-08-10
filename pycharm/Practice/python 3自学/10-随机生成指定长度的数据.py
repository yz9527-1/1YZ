'''
#1.利用string基本上可以获取字符串所有的组成元素。

import string
print(string.punctuation)
#输出为：!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.digits)
#输出为：0123456789
print(string.ascii_letters)
#输出为：abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# 2.random模块

import random
print(random.random())
#0.21005996137264848，random.random()在0-1之间随机选择一个浮点型的数
print(random.randint(1,10))
#2，random.randint(a,b)在[a,b]之前随机选择一个整数
print(random.randrange(10,100,2))
#90，random.randrange(a,b,num)表示从[a,b]以num行程的等差数列中选择一个数。
print(random.choice('python'))
#t，random.choice(list)从list中选择一个元素
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
print(random.sample(list, 6))
#[11, 5, 12, 6, 8, 3]，从list中随机选择6个数

#3.随机获取8位字符串。获取思路，从字符串有效元素中获取8个然后组合成一个新的字符串

可用于自动化测试生成数据，或者生成随机密码。

import string,random
goal = ''.join(random.sample(string.ascii_letters+string.digits+string.punctuation,8))
print(goal)
#Qj|V)*kd

#for i in range(15):
       # a="测试%d"%(i)
       # print(a)
'''
x=5
def printfuc():
    y=2
    z=3
    print(y+z)
    print(z)
printfuc()
print(y)
print(x)