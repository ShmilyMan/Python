# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 21:05
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.函数参数传递的内存分析.py
# @Software: PyCharm

'''
    函数参数的传递规律：
    当函数进行参数传递时，
    如果传递的不可变对象，则形参的改变不会引起实参的改变，相当于值传递
    如果传递的是可变对象，则相对应的形参的改变会引起实参的改变（形参和实参都指向相同的内存地址，相当于地址传递）
'''
def fun(arg1,arg2):
    print('arg1 = ',arg1) # 11
    print('arg2 = ',arg2) # [22, 33, 44]
    arg1 = 100
    arg2.append(99)
    print('arg1 = ', arg1) # 100
    print('arg2 = ', arg2) # arg2 =  [22, 33, 44, 99]


n1 = 11
n2 = [22,33,44]
print('n1 = ',n1) # 11
print('n2 = ',n2) # [22, 33, 44]
fun(n1,n2)
print('n1 = ',n1) # 11
print('n2 = ',n2) # arg2 =  [22, 33, 44, 99]

