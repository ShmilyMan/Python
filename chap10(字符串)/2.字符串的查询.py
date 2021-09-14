# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:45
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.字符串的查询.py
# @Software: PyCharm

'''
    字符串的查询：
        1.index()：查找第一个字符串出现的位置
        2.rindex()：查找最后一个字符串出现的位置
        3.find()：查找第一个字符串出现的位置
        4.rfind()：查找最后一个字符串出现的位置
    注意：index方法当字符串不存在时会抛出异常
          find方法当所查找的字符串不存在时返回值-1
'''
str1 = 'hellow,hwllow'
print(str1.index('lo')) # 3
print(str1.find('lo')) # 3
print(str1.rindex('lo')) # 10
print(str1.rfind('lo')) # 10

print('--------所查找的字符串不存在时---------')
print(str1.find('k')) # -1
print(str1.index('pp')) # ValueError: substring not found   报错