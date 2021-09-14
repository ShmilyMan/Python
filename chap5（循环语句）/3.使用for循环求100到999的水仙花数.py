# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 10:04
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.使用for循环求100到999的水仙花数.py
# @Software: PyCharm
print('水仙花数为：')
for num in range(100,1000):
    num1 = num // 100     # 个位
    num2 = num % 10       # 百位
    num3 = num // 10 % 10 # 十位
    if num == num1**3 + num2**3 + num3**3:
        print(num)