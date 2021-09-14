# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 20:09
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 5.函数参数的总结.py
# @Software: PyCharm

'''1.使用列表分别对位置参数进行赋值'''
# 函数定义
def fun(a,b,c):
    print('a = ',a)
    print('b = ', b)
    print('c = ', c)

# 函数调用
lst = [10,20,30]
fun(*lst) # 此时在列表参数前面加一个*号，分别将列表中的数据传递给函数的形参

'''2.使用字典分别对关键字参数进行赋值'''
# 函数定义
def fun2(a,b,c):
    print('a = ',a,'b = ',b,'c = ',c)

# 函数调用
dic = {'a':11,'b':22,'c':33}
fun2(**dic) # 此时在字典参数前面加两个*号

'''3.指定某个参数后边必须使用位置实参进行赋值'''
def fun3(a,b,*,c,d):
    print('fun3...，在*号后边的参数必须使用位置实参进行赋值')

fun3(10,20,c=30,d=40) # fun3...，在*号后边的参数必须使用位置实参进行赋值

'''4.函数中参数的定义顺序'''
# 以下三种形式均是可以的
def fun4(a,b,c = 10,*d,**e):
    pass

def fun5(*a,**b):
    pass

def fun6(a,b = 20,*,c = 10,**f):
    pass
