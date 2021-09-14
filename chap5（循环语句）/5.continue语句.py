# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 10:36
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 5.continue语句.py
# @Software: PyCharm

'''使用continue输出1-50之间所有5的倍数'''
for item in range(1,51):
    if item % 5 != 0:
        continue
    else:
        print(item)