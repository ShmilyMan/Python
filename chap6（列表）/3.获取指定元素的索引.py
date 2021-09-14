# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 17:17
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.获取指定元素的索引.py
# @Software: PyCharm

lst = ['hellow','world','hellow',98]

print(lst.index('hellow')) # 0 当列表中存在相同的元素的时候，所找到的是第一个出现的元素的索引
# print(lst.index('ddd')) # 报错 'ddd' is not in list,元素在列表中不存在
print(lst.index('hellow',1,3)) # 2 -- > 在大于1小于3的索引中进行查找