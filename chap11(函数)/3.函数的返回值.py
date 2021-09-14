# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 21:16
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.函数的返回值.py
# @Software: PyCharm

'''
    1.当函数没有返回值时，可以不写return语句或直接写return
    2.当函数有一个返回值时，return ...返回要返回的数据类型
    3.当函数有两个以上的返回值时，可以返回多个返回值，返回的格式是一个元组（元组是不可变的数据类型）
'''

'''求一个列表中的奇数和偶数所形成的列表'''
def fun(num):
    odd = [] # 存放奇数
    even = [] # 存放偶数
    for temp in num:
        if temp % 2:
            odd.append(temp)
        else:
            even.append(temp)
    return odd,even


n = fun([1,2,3,4,5,6,7,8,9,10,11])
print(n) # ([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10])
print(n[0]) # [1, 3, 5, 7, 9, 11]
print(n[1]) # [2, 4, 6, 8, 10]
print(n[1::])# ([2, 4, 6, 8, 10],) 元组切片的结果还是为元组
