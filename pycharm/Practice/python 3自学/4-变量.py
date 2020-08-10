# 这里介绍 变量

# 变量可以是数字
var1 = 5
print(var1)

# 变量可以是字符
var2 = 'hello'
print(var2)

# 变量可以是运算表达式
var3 = 5 + 67
print(var3)

# 变量可以是函数
var4 = print('hello Python 3')

"""
总结：
变量的命名规范

1、变量名可以包括字母、数字、下划线，但是数字不能做为开头。例如：name1是合法变量名，而1name就不可以。
2、系统关键字不能做变量名使用
3、除了下划线之个，其它符号不能做为变量名使用
4、Python的变量名是除分大小写的，例如：name和Name就是两个变量名，而非相同变量

"""
from pycharm.Practice.common.Sort import Sort
list1=[1,9,15,84,75,65,31,26,94,57]
print(Sort.quick_sort(list1))