# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 18:59
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.字典元素的获取.py
# @Software: PyCharm

scores = {'张三':98,'李四':88,'王五':37}
'''1.使用[]获取字典元素'''
print(scores['张三']) # 98
# print(scores['麻六']) # KeyError: '麻六'如果所查找的值不存在，则会报错

'''2.使用get()函数获取字典元素'''
print(scores.get('张三')) # 98
print(scores.get('麻六')) # None 所查找的值不存在，则会输出None
# 当所查找的值不存在时，可以给那个不存在的值赋予一个默认的值
print(scores.get('麻六',100))

