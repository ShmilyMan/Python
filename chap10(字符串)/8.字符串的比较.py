# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:48
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 8.字符串的比较.py
# @Software: PyCharm

'''
    字符串的比较操作：
        可以使用>,<,>=,<=,==,!=来进行字符串的比较，实际上是比较字符串中每个字符的值
        注意：==是比较字符串中的值是否相等
              is是用于比较两个字符串的id是否相等
'''

str1 = 'python'
str2 = 'python'

print(str1 == str2) # True
print(str1 is str2) # True 字符串的驻留机制导致两个字符串在内存中的存储地址相同