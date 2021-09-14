# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:46
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.字符串的大小写转换.py
# @Software: PyCharm

'''
    字符串的大小写转换：转化将产生一个新的字符串
        1.upper()：将字符串中所有的字符转化成大写
        2.lower()：将字符串中所有的字符转化成小写
        3.swapcase()：将字符串中所有的大写字母转化成小写字母，将字符串中所有的小写字母转化成大写
        4.capitalize()：将字符串中第一个字符转化成大写，其余的转化成小写
        5.title()：将字符串中所有字母的第一个字母转化成大写，把每个单词的其余字母转化成小写
'''
str1 = 'hallow python'

print(str1.upper()) # HALLOW PYTHON
print(str1.lower()) # hallow python
print(str1.swapcase()) # HALLOW PYTHON
print(str1.capitalize()) # Hallow python
print(str1.title()) # Hallow Python
