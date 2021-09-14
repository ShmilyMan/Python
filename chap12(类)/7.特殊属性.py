# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 23:04
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 7.特殊属性.py
# @Software: PyCharm

class A:
    pass

class B:
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

class D(A):
    pass


c = C('张三', 24)
print(c.__dict__) # 输出的是该对象中所有属性的字典  {'name': '张三', 'age': 24}
print(C.__dict__) # 输出C类中的方法和属性  {'__module__': '__main__', '__init__': <function C.__init__ at 0x000001B4EFE6BF28>, '__doc__': None}
print('----------------------')
print(c.__class__) # 输出该对象所属的类  <class '__main__.C'>
print(C.__bases__) # 输出该类的父类  (<class '__main__.A'>, <class '__main__.B'>)
print(A.__subclasses__()) # 输出该类的所有子类  [<class '__main__.C'>, <class '__main__.D'>]
print('-------输出类的层次结构-------')
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

