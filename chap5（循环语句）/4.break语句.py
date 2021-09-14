# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 10:29
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.break语句.py
# @Software: PyCharm

'''银行取款（使用for语句实现）'''
# for item in range(3):
#     pwd = input('请输入密码：')
#     if pwd == '8888':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')

'''银行取款（使用while语句实现）'''
item = 0
while item < 3:
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    item += 1
