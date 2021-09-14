# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 18:10
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 6.列表元素的判断和遍历.py
# @Software: PyCharm

lst = ['hello','world',97,'python']

'''可以使用 in 或 not in 来判断一个元素是否在列表中存在'''
print('hello' in lst)    # True
print('hello' not in lst)# False

'''列表的遍历'''
print('------------------------')
for item in lst:
    print(item)