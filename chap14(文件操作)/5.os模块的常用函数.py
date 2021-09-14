# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 21:36
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 5.os模块的常用函数.py
# @Software: PyCharm

'''
    os模块操作目录的函数：
        1.getcwd():获取当前的工作目录
        2.listdir(path):返回指定路径下的文件和目录的信息
        3.mkdir(path[,mode]):创建目录
        4.makedirs(path/path...[,mode]):创建多级目录
        5.rmdir(path):删除目录
        6.removedirs(path1/path2...):删除多级目录
        7.chdir(path):将path设置为当前工作目录
'''
import os
print(os.getcwd()) # D:\PythonWorkspace\chap14(文件操作)
print(os.listdir('../chap14(文件操作)')) # ['1.读取指定文件的内容.py', '2.常用文件的打开方式.py', '3.文件对象的常用方法.py', '4.with语句.py', '5.os模块的常用函数.py', 'a.jpg', 'b.jpg', 'b.txt', 'c.txt', 'copya.jpg']
# print(os.mkdir('A'))
# print(os.makedirs('B/D/F'))
# os.rmdir('A')
# os.removedirs('B/D/F')
os.chdir('../chap12(类)')
print(os.getcwd())