# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:21
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 1.while循环.py
# @Software: PyCharm
'''计算0~4的和（使用while循环）'''
sum = 0
i = 0
while i < 5:
    sum += i
    i += 1
print('0~4的和为',sum) # 10

sum = 0
'''计算1~100的偶数和'''
i = 1
while i <= 100:
    if not (i % 2):
       sum += i
    i += 1
print('1~100的偶数和为',sum) # 2550