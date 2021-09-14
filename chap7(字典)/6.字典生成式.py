# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 19:49
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 6.字典生成式.py
# @Software: PyCharm

'''将两个列表合并成一个字典'''
# 当两个列表的长度不同时，以长度小的列表为基准
items = ['Frults','App','Other']
values = [88,99,100]

dic = {item.upper() : value for item,value in zip(items,values)}
print(dic) # {'FRULTS': 88, 'APP': 99, 'OTHER': 100}