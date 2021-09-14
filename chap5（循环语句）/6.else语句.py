# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 10:52
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 6.else语句.py
# @Software: PyCharm

'''
    else语句和for，while连用的情况：
        遇到break语句时不会执行，否则当循环执行结束时执行else语句的部分
'''
for _ in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码输入正确')
        break
    else:
        print('密码输入错误')
else:
    print('对不起，三次密码均输入错误')
