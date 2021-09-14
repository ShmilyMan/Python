# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 23:13
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.文件对象的常用方法.py
# @Software: PyCharm

'''
    文件对象的常用方法：
        1.read([size]):从文件中读取size个字节或字符的内容，若省略size则读取到文件末尾，即一次读取文件的所有内容
        2.readline():从文本文件中读取一行内容
        3.readlines():把文本中每一行都作为独立的字符串对象，并将这个对象放进列表中返回
        4.write(str):将字符串的内容写进文件
        5.writelines(s_list):将字符串列表写进文件
        6.seek(offset[,whence]):把文件的指针移动到新的位置
            whence不同的值代表不同的含义：
                0：从文件头开始计算
                1：从当前位置开始计算
                2：从文件尾开始计算
        7.tell()：返回文件指针当前的位置
        8.flush()：把缓冲区的内容写入文件，但不关闭文件
        9.close():把缓冲区的内容写入文件，并关闭文件，释放文件对象相关的资源

    注意：一个中文的汉字占两个字节
'''
file1 = open('b.txt', 'r')
file1.seek(2)
print(file1.read())
print(file1.tell())
file1.close()

# lst = ['a','b','c']
# file2 = open('c.txt', 'w')
# file2.write('hello')
# file2.writelines(lst)
# file2.close()
