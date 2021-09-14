# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 17:26
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.以主程序的方式运行.py
# @Software: PyCharm

import cala

print(cala.add(6,78)) # 84

import package1.modal1 as ma
from package1 import modal1

'''包的使用'''
print(ma.a) # 10
print(modal1.a) # 10