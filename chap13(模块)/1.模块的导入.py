# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 17:08
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 1.模块的导入.py
# @Software: PyCharm
'''
    导入模块的方式：
        1.import 模块名 [as 别名]：导入模块的整个内容
        2.from 模块名 import 导入函数/变量/类
'''
'''1.导入系统的模块'''
# import math
# print(dir(math)) # 获取math模块所有的属性和方法
# print(math.pi) # 3.141592653589793
# print(math.pow(2,3)) # 8.0

# from math import pow
# print(pow(2,3)) # 8.0

'''2.导入自己定义的模块'''
import cala
print(cala.add(3,5)) # 8

from cala import add
print(add(3,9)) # 12
