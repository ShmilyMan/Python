# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 5.字符串的劈分.py
# @Software: PyCharm

'''
    字符串的劈分：
        1.split()：从左侧对字符串进行劈分
        2.rsplit()：从右侧对字符串进行劈分

    注意：
        1.可以通过参数sep指定劈分符,默认的劈分符为空格
        2.可以通过参数maxsplit指定劈分的最大次数
        3.字符串劈分的结果为一个列表
'''

str1 = 'hallow|world|python'

print(str1.split(sep='|',maxsplit=1)) # ['hallow', 'world|python']
print(str1.rsplit(sep='|',maxsplit=1)) # ['hallow|world', 'python']