# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:00
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 5.集合生成式.py
# @Software: PyCharm

s = {i for i in range(6)}
print(s) # {0, 1, 2, 3, 4, 5}

# 获取集合的元素,不能直接获取集合中的元素，可以将集合中的元素转成列表再进行索引操作
lst = list(s) # 将集合转化成列表
for temp in lst:
    print(temp)