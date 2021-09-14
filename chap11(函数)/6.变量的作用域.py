# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 20:30
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 6.变量的作用域.py
# @Software: PyCharm

'''
    局部变量：在函数内部定义的变量，只在函数内部有效，局部变量使用global声明，则他就会变成全局变量
    全局变量：函数体外定义的变量，可用于函数体的内外
'''

# global声明局部变量的实例
def fun():
    global age # 使用global声明局部变量，则他变为全局变量
    age = 10
    print('函数体内age = ',age) # 函数体内age =  10

fun()
print('函数体外age = ',age) # 函数体外age =  10