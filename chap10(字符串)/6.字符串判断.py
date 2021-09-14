# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 6.字符串判断.py
# @Software: PyCharm

'''
    字符串的判断：
        1.isidentifier()：判断指定的字符串是否为合法的标识符（字母，数字，下划线）
        2.isspace()：判断指定的字符串是否全部为空白字符组成（回车，换行，水平制表符）
        3.isalpha()：判断指定的字符串是否全部由字母组成
        4.isdecimal()：判断指定的字符串是否全部由十进制数字组成
        5.isalnum()：判断指定的字符串是否全部由字母数字组成(此方法中，大写的数字如一，二...罗马数字都被认为是数字)
'''

# 1.isidentifier()
print('dcsd'.isidentifier()) # True
print('scas!'.isidentifier()) # False

# 2.isspace()
print('\t'.isspace()) # True
print(' '.isspace()) # True
print(''.isspace()) # False 为空字符串

# 3.isalpha()
print('张三'.isalpha()) # True

# 4.isdecimal()
print('123四'.isdecimal()) # False
print('2515'.isdecimal()) # True

# 5.isalnum()
print('123四'.isalnum()) # True
