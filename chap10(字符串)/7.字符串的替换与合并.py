# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 7.字符串的替换与合并.py
# @Software: PyCharm

'''
    1.字符串的替换：
        replace()：第一个参数指定要替换的字符串，第二个参数指定替换子串的字符串，第三个参数指定替换的最大次数,
        默认的进行全部替换
    2.字符串的合并：
        join()：将列表或元组中的字符串合并成一个字符串
'''

# 1.replace()
print('hallow python python python'.replace('python','java',2)) # hallow java java python

# 2.join()
print('*'.join(['hallow','python','python'])) # 用*号连接列表中的元素 hallow*python*python
print(''.join(('hallow','python','python'))) # 用空字符连接元组 hallowpythonpython
print('*'.join('hallow')) # h*a*l*l*o*w