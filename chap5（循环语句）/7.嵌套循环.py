# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 12:23
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 7.嵌套循环.py
# @Software: PyCharm

'''99乘法表'''
for i in range(1,10):
    for j in range(1,i + 1):
        print(j,' * ',i,' = ',i * j,end='\t')
    print()