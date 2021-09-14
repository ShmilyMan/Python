# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 10:40
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 1.类的定义.py
# @Software: PyCharm

class Student:
    #name = '' # 全局属性，使用Student调用
    #age = 0
    gender = '男' # 类属性，相当于static public，通过类名或类的实例化对象进行调用

    # 初始化类的属性的方法
    def __init__(self,name,age): # 类的实例属性，只能使用类的实例化对象进行调用
        self.name = name
        self.age = age

    # 实例方法
    def info(self):
        print('我是实例化方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法')

    # 静态方法
    @staticmethod
    def sm():
        print('我是静态方法')

# 初始化类的实例化对象
student = Student('张三', 23)
print(student.age) # 23
print(student.name) # 张三

# 调用类的实例化方法,使用类的实例和使用类都可以调用，当使用类进行调用时要传该类的实例化对象
student.info() # 我是实例化方法
Student.info(student) # 我是实例化方法

# 类方法和静态方法的调用
Student.cm() # 我是类方法
Student.sm() # 我是静态方法

