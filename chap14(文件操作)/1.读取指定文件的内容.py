# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 22:36
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 1.读取指定文件的内容.py
# @Software: PyCharm
file = open('D://a.txt','r')
print(file.readlines()) # ['阿洒水车\n', '抽刀断水\n', '小学生']
file.close()
