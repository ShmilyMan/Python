# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 21:12
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.Python中常用的内容模块.py
# @Software: PyCharm

'''1.sys：与python解释器及其环境操作相关的标准库'''
import sys
# 获取所占的字节数,一个字节占8位
print(sys.getsizeof(45)) # 28
print(sys.getsizeof(True)) # 28
print(sys.getsizeof(False)) # 24

'''2.time：提供与时间相关的各种函数的标准库'''
import time
print(time.time()) # 1606483024.143392
# 转化成本地的时间
print(time.localtime(time.time())) # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=27, tm_hour=21, tm_min=17, tm_sec=33, tm_wday=4, tm_yday=332, tm_isdst=0)

'''3.urllib：用于读取来自网上（服务器）的数据标准库'''
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com/more/').read())

'''4.schedule模块的使用'''
import schedule

def show():
    print('哈哈...')

schedule.every(3).seconds.do(show) # 每三秒执行一次show方法
while True:
    schedule.run_pending()
    time.sleep(1) # 睡眠1秒