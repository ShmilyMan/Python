# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 12:35
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 8.获取指定目录下的所有文件和目录.py
# @Software: PyCharm

import os

path = os.getcwd()
listdir = os.listdir(path)
for fileName in listdir:
    if fileName.endswith('.py'):
        print(fileName)
