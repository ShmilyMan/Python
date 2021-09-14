# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 16:13
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : chap6(列表).py
# @Software: PyCharm

'''
    变量保存的是一个对象的引用
    而列表保存的是多个对象的引用，一个列表有它自己的ID
    列表中存储的是内存中每个对象的地址
    而且列表中存储的数据类型可以不同
    --> 相当于其他语言中的数组
'''
a = 10
lit = ['hallow','world',89]
print(id(lit))   # 列表的id
print(type(lit)) # 列表的类型
print(lit)       # 输出列表对象