# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 20:30
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 10.列表元素的排序操作.py
# @Software: PyCharm

lst = [10,5,50,44,88,77]

# 1.使用list对象的sort()函数进行排序，默认为升序，可以使用reverse进行降序排序，排序不会产生新的列表
lst.sort() # 升序排序
print(lst) # [5, 10, 44, 50, 77, 88]

lst.sort(reverse=True) # 指定参数进行降序排序
print(lst) # [88, 77, 50, 44, 10, 5]

# 2.使用内置对象sorted()函数进行排序，默认为升序，可以使用reverse进行降序排序，排序将会产生新的列表
new_list = sorted(lst) # 升序
print(new_list) # [5, 10, 44, 50, 77, 88]

new_list = sorted(lst, reverse=True) # 降序
print(new_list) # [88, 77, 50, 44, 10, 5]
