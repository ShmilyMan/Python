# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 17:15
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : cala.py
# @Software: PyCharm

def add(x,y):
    return x + y

if __name__ == '__main__':
    print(add(3, 4))  # 相当于main函数，在别的模块导入该模块的时候不会运行该部分的代码，只有在运行本模块的时候才会执行该部分的代码
