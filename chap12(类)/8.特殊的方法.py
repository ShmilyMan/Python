# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 13:08
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 8.特殊的方法.py
# @Software: PyCharm

class Student:
    def __init__(self,name):
        self.name = name

    def __add__(self, other): # 重写__add__方法
        return self.name + other.name

    def __len__(self): # 重写__len__方法
        return len(self.name)

'''1.__add__():通过重写该方法可使自定义的对象具有'+'的功能'''
student1 = Student('张三')
student2 = Student('李四')
print(student1 + student2) # 张三李四

'''2.__len__()：重写该方法，可以使自定义对象具有求长度的功能'''
print(student1.__len__()) # 2
print(len(student1)) # 2  len()实际调用的是对象的__len__方法

'''3.__new__()：用于创建对象，__init__()：用于初始化对象'''
class People:
    def __new__(cls, *args, **kwargs):
        print('People的对象被执行了，他的id为{0}'.format(id(cls))) # 2313705688152
        obj = super().__new__(cls)
        print('obj对象被创建了，他的id为{0}'.format(id(obj))) # 2313736463696
        return obj

    def __init__(self,name):
        print('init方法被执行了，self的id为{0}'.format(id(self))) # 2313736463696
        self.name = name

print('Object类的id：',id(object)) # 1395377536
print('People类的id：',id(People)) # 2313705688152

people = People('张三')
print('people对象的id：',id(people)) # 2313736463696

