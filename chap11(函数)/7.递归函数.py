# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 20:36
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 7.递归函数.py
# @Software: PyCharm

'''计算一个数的阶乘'''
# 函数定义
def fun(n):
    if n == 1:
        return 1;
    else:
        return n * fun(n - 1)

# 函数调用,计算6的阶乘
print(fun(6)) # 720