# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 18:28
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 7.列表的添加操作.py
# @Software: PyCharm

lst = [10,20,30,40,50]
print('原列表：',lst)

print('-----------在列表的末尾添加一个元素-------------')
lst.append(60)
print(lst)

print('-------------在列表的末尾添加至少一个元素-----------------')
lst2 = ['a','b']
lst.extend(lst2)
print(lst)

print('-----------在列表的任意位置添加一个元素-------------')
lst.insert(1,'hello') # 其余的元素向后移
print(lst)

print('----------在列表的任意一个位置添加至少一个元素（切片）-------------')
lst[1:] = [20,30,90]
lst[1] = 98
print(lst)