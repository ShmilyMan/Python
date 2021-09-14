# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 10:46
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.字符串的内容对齐.py
# @Software: PyCharm

'''
    字符串的内容对齐：
        1.center()：居中对齐，第一个参数指定宽度，第二个参数指定填充符
        2.ljust()：左对齐,第一个参数指定宽度，第二个参数指定填充符
        3.rjust()：右对齐，第一个参数指定宽度，第二个参数指定填充符
        4.zfill()：右对齐，参数指定宽度，用零填充

    注意：
        1.默认的填充符为空格
        2.当指定的宽度小于字符串的长度时，将输出原来的字符串
'''

str1 = 'hallow python'
print(str1.center(20,'*')) # ***hallow python****
print(str1.ljust(20,'*')) # hallow python*******
print(str1.rjust(20,'*')) # *******hallow python
print(str1.zfill(20)) # 0000000hallow python

print('-5555'.zfill(9)) # -00005555