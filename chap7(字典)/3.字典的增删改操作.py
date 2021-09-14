# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 19:07
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.字典的增删改操作.py
# @Software: PyCharm

scores = {'张三':98,'李四':88,'王五':37}
'''判断指定的键是否的字典中'''
print('张三' in scores) #True
print('张三' not in scores) # False

'''增加字典的元素'''
scores['麻六'] = 55
print(scores) # {'张三': 98, '李四': 88, '王五': 37, '麻六': 55}

'''删除字典中的元素'''
del scores['张三']
print(scores) # {'李四': 88, '王五': 37, '麻六': 55}

# scores.clear() # 清空字典中的元素
# print(scores) # {}

'''修改字典中的元素'''
scores['李四'] = 100
print(scores) # {'李四': 100, '王五': 37, '麻六': 55}
