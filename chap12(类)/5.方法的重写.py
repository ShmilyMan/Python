# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 17:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 4.类的继承和实现方式.py
# @Software: PyCharm
'''
    方法的重写：
        1.如果子类对继承于父类的某个方法或属性不满意，可以在子类中对其方法体重新编写
        2.子类重写后的方法可以通过super.xxx()调用父类中被重写的方法
'''
class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def show(self):
        print('name = ',self.__name,' age = ',self.__age)

    def __str__(self) -> str:
        return '我是%s,今年%d岁了' % (self.__name,self.__age)


people = People('张三', 58)
print(people)


class Studet(People):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.__score = score

    def show(self):
        super().show()
        print('score = ',self.__score)


class Teacher(People):
    def __init__(self,name,age,teacherOfAge):
        super().__init__(name,age)
        self.__teacherOfAge = teacherOfAge

    def show(self):
        super().show()
        print('teacherOfAge = ',self.__teacherOfAge)



studet = Studet('张三', 24, 89.98)
teacher = Teacher('李四', 39, 15)
studet.show() # name =  张三  age =  24    score =  89.98
teacher.show() # name =  李四  age =  39   teacherOfAge =  15
