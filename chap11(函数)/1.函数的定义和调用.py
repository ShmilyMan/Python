# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:48
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 11.字符串的编码与解码.py
# @Software: PyCharm

'''函数的定义'''
def cala(a,b):
    c = a + b
    return c

'''函数的调用，函数必须先定义后调用'''
print(cala(10,20)) # 30

print(cala(b=20,a=50)) # 70  等号左侧的名称为关键字参数，使用了关键字参数后函数的参数传递就不会按照位置传递
