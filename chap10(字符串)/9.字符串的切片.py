# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:48
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 9.字符串的切片.py
# @Software: PyCharm

'''
    字符串的切片操作：
    形式：[start:stop:step]
    start:如果不写，则默认为0开始
    stop：如果不写，则默认到最后一个字符结束
    step：如果不写，默认为1
'''

str1 = 'hallow,Python'
print(str1[:6] + '!' + str1[7::]) # hallow!Python