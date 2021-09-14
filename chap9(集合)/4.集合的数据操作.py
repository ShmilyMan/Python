# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 9:59
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.集合的数据操作.py
# @Software: PyCharm

s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
'''1.集合的交集'''
print(s1.intersection(s2))
print(s1 & s2) # {40, 20, 30}

'''2.集合的并集'''
print(s1.union(s2))
print(s1 | s2) # {40, 10, 50, 20, 60, 30} 去掉了相同的元素，将两个集合合并

'''3.集合的差集'''
print(s1.difference(s2))
print(s1 - s2) # {10} 属于s1而不属于s2

'''4.集合的对称差集'''
print(s1.symmetric_difference(s2))
print(s1 ^ s2) # {50, 10, 60} s1并s2再去掉相交的部分