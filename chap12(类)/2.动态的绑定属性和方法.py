# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 16:43
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 2.动态的绑定属性和方法.py
# @Software: PyCharm

'''Python是动态语言，在创建类的对象后，可以动态的为这个对象添加属性和方法，所添加的方法只限于本类中使用'''
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 实例化方法
    def eat(self):
        print(self.name,'  ',self.age)


people = People('张三', 23)
# 动态的为people实例化对象添加属性
people.gender = '女'
print(people.gender) # 女

# 动态的为people实例化对象添加方法
def look():
    print('该方法为动态的为类的实例化对象添加的方法')

people.look = look
people.look() # 该方法为动态的为类的实例化对象添加的方法（即把一个函数绑定到这个类的实例化对象中）

