# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 12:39
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 9.递归的获取指定目录下的所有文件和目录.py
# @Software: PyCharm

import os

path = os.getcwd()
walk = os.walk(path)

for dirpath,dirnames,filenames in walk:
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print('---------------------')
    for filename in filenames:
        print(os.path.join(dirpath,filename))
    for dirname in dirnames:
        print(os.path.join(dirpath,dirname))
    print('----------------------')
