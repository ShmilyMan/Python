# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 20:14
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 1.元组的创建.py
# @Software: PyCharm

# 元组被定义成不可变的序列
'''1.使用()创建'''
t1 = ('Python', 'Hallow', 'world')
print(t1) # ('Python', 'Hallow', 'world')

# 可以不使用()创建元组
t2= 'Python', 'Hallow', 'world'
print(t2) # ('Python', 'Hallow', 'world')

# 当要创建只有一个元素的元组时，注意加上逗号，否则会被当做是字符串进行处理
t3 = ('Python') # 不加逗号，被当做字符串进行处理
print(t3,type(t3)) # Python <class 'str'>
t4 = ('Python',) # 加逗号，被当做元组进行处理
print(t4,type(t4)) # ('Python',) <class 'tuple'>

'''2.使用内置函数进行创建'''
t5 = tuple(('Python', 'Hallow', 'world'))
print(t5) # ('Python', 'Hallow', 'world')

'''3.创建空元组'''
t6 = ()
t7 = tuple()
print(t6) # ()
print(t7) # ()
