# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 12:18
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 7.os.path模块操作目录的函数.py
# @Software: PyCharm

'''
    1.abspath():获取文件或目录的绝对路径
    2.exists():用于判断文件或目录是否存在
    3.join(path,name):将目录与目录或者文件名拼接起来
    4.splitext():分离文件名或扩展名
    5.basename():从一个目录中提取文件名
    6.dirname():从一个路径中提取文件路径路径，不包括文件名
    7.isdir():用于判断是否为路径
'''
import os.path
print(os.path.abspath('4.with语句.py')) # D:\PythonWorkspace\chap14(文件操作)\4.with语句.py
print(os.path.exists('4.with语句.py'),os.path.exists('sss.py')) # True False
print(os.path.join('D:\\PythonWorkspace\\chap14(文件操作)','4.with语句.py')) # D:\PythonWorkspace\chap14(文件操作)\4.with语句.py
print(os.path.splitext('4.with语句.py')) # ('4.with语句', '.py')
print(os.path.basename('D:\\PythonWorkspace\\chap14(文件操作)\\4.with语句.py')) # 4.with语句.py
print(os.path.dirname('D:\\PythonWorkspace\\chap14(文件操作)\\4.with语句.py')) # D:\PythonWorkspace\chap14(文件操作)
print(os.path.isdir('D:\PythonWorkspace\chap14(文件操作)')) # True