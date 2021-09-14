# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 20:36
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 8.斐波那契数列.py
# @Software: PyCharm

def fib(n): # 求第n位的斐波那契数列中的数字
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# 输出斐波那契数列第六位的数字
print(fib(6)) # 8

# 输出斐波那契数列前六位的数字
for temp in range(1,7):
    print(fib(temp),end='\t') # 1	1	2	3	5	8