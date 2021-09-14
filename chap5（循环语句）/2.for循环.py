# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 16:54
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.for循环.py
# @Software: PyCharm
# for 变量 in 可以迭代的对象：字符串，列表，range（）函数产生的对象
# 把后边儿的值依次赋值给前面的变量
# 字符串
for item in 'Python':
    print(item)
#range()函数产生的对象
for item in range(10): # item会自动的加一
    print(item)

print('使用for循环计算1~100的偶数和')
sum = 0
for item in range(1,101):
    if item % 2 == 0:
        sum += item
print("1~100的和为：",sum)

# 当不需要给变量赋值时，可以使用_进行代替
for _ in range(5): # 值0 - 4
    print('wxl') # 此时不需要变量，循环执行5次