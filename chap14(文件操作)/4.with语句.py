# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 21:28
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.with语句.py
# @Software: PyCharm

'''with语句可以自动的管理上下文资源，不论什么原因跳出with块，都能确保文件能正常关闭，以此达到释放资源的目的'''
with open('b.txt','r') as file:
    print(file.read())

# 使用with语句进行文件的拷贝
with open('a.jpg','rb') as src_file:
    with open('b.jpg','wb') as dest_file:
        dest_file.write(src_file.read())