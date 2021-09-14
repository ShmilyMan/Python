# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 17:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.类的继承和实现方式.py
# @Software: PyCharm
'''
    1.继承的语法形式：
        class 子类名(父类1,父类2):
            pass
    2.如果一个类中没有继承任何类，则默认继承object类
    3.Python支持多继承
    4.定义子类时，必须在子类的构造函数中调用父类的构造函数
'''
class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def show(self):
        print('name = ',self.__name,' age = ',self.__age)

class Studet(People):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.__score = score

class Teacher(People):
    def __init__(self,name,age,teacherOfAge):
        super().__init__(name,age)
        self.__teacherOfAge = teacherOfAge


studet = Studet('张三', 24, 89.98)
teacher = Teacher('李四', 39, 15)
studet.show() # name =  张三  age =  24
teacher.show() # name =  李四  age =  39
