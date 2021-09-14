# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 9:44
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.集合间的关系.py
# @Software: PyCharm

s1 = {10,20,30,40}
s2 = {20,10,30,40}
s3 = {10,20,30,40,50,60}
s4 = {100,200,300}
'''1.判断两个集合是否相等，如果两个集合的元素相同，则认为相等'''
print(s1 == s2) # True
print(s1 == s3) # False

'''2.判断一个集合是否为另一个集合的子集'''
print(s1.issubset(s3)) # True
print(s1.issubset(s4)) # False

'''3.判断一个集合是否为另一个集合的超集'''
print(s3.issuperset(s1)) # True
print(s4.issuperset(s1)) # False

'''4.判断集合是否没有交集'''
print(s3.isdisjoint(s1)) # False
print(s3.isdisjoint(s4)) # True