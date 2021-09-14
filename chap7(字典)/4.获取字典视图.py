# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 19:25
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.获取字典视图.py
# @Software: PyCharm

scores = {'张三':98,'李四':88,'王五':37}
'''获取字典所有的keys'''
keys = scores.keys()
print(keys) # dict_keys(['张三', '李四', '王五'])
print(list(keys)) # 转化成列表 ['张三', '李四', '王五']

'''获取字典所有的值'''
values = scores.values()
print(values) # dict_values([98, 88, 37])
# 转化为列表
print(list(values)) # [98, 88, 37]

'''获取字典所有的键值对'''
items = scores.items()
print(items) # dict_items([('张三', 98), ('李四', 88), ('王五', 37)])
# 转化成列表
print(list(items)) # [('张三', 98), ('李四', 88), ('王五', 37)] 列表中的每个元素由一个一个元组构成
