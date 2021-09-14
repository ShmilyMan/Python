# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 22:41
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.常用文件的打开方式.py
# @Software: PyCharm

'''
    文件的常用打开方式：
        1.r：以只读的方式打开
        2.w：以只写的方式打开，如果文件不存在则创建文件，再次写入内容时会覆盖文件的内容
        3.a：以追加的方式打开，如果文件不存在则创建文件
        4.b：以二进制的方式打开，不能单独使用
        5.+：以读写的方式打开，不能单独使用，如a+
'''
'''1.创建文件，并写入内容'''
file1 = open('b.txt', 'w')
file1.write('sdsdsw')
file1.close()

'''2.进行图片的复制'''
src_file = open('a.jpg', 'rb') # 以二进制的方式打开
dest_file = open('copya.jpg', 'wb')

dest_file.write(src_file.read())

src_file.close() # 关闭资源
dest_file.close()
