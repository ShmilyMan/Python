# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 16:13
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 9.浅拷贝与深拷贝.py
# @Software: PyCharm
class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

'''1.浅拷贝：Python中的拷贝一般是浅拷贝，拷贝时，对象包含的子对象的内容不拷贝，源对象与拷贝对象引用同一个子对象'''
cpu = Cpu()
disk = Disk()

computer = Computer(cpu, disk)
import copy

computer2 = copy.copy(computer)
# 拷贝的过程中只拷贝了源对象，而源对象中包含的两个子对象，所以拷贝对象和源对象中子对象的内存地址是相同的
print(id(computer),' ',id(computer.cpu),' ',id(computer.disk)) # 2823608050576   2823607987952   2823608050520
print(id(computer2),' ',id(computer2.cpu),' ',id(computer2.disk)) # 2823608050632   2823607987952   2823608050520

'''2.深拷贝：递归拷贝对象中包含的子对象，源对象和拷贝对象的所有的子对象也不相同'''
computer3 = copy.deepcopy(computer)
# 拷贝的过程中，对源对象中所有的子对象也进行了递归的拷贝，拷贝后，拷贝对象及他的子对象的内存地址与源对象都不相同
print(id(computer),' ',id(computer.cpu),' ',id(computer.disk)) # 1349993735000   1349993670360   1349993672432
print(id(computer3),' ',id(computer3.cpu),' ',id(computer3.disk)) # 1349993735280   1349993736736   1349993813048
