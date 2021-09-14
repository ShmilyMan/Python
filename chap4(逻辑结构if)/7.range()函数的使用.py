# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:04
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : range()函数的使用.py
# @Software: PyCharm
# range()函数：用于生成一个整数的序列,生成的序列是左闭右开的
'''
    优点：不管所表示的序列多大，存储所占的内存中的空间相同
        存储：初始值，最终值和步长
'''
'''1.只有一个参数，默认从0开始，步长为1'''
r = range(10)
print(list(r)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''2.有两个参数，默认步长为1'''
r = range(1,10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(r))

'''3.有三个参数，三个参数分别是初始值，结束值和步长'''
r = range(1,10,2)
print(list(r)) # [1, 3, 5, 7, 9]

'''4.可以使用in或not in来判断一个整数是否在range()函数生成的序列中'''
print(10 in r) # False
print(10 not in r) # True
print(9 in r) # True
print(9 not in r) # False
