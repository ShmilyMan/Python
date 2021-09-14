# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 22:52
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 6.多态性.py
# @Software: PyCharm
'''
    动态语言中的多态性：鸭子类型
'''
class Animal:
    def eat(self):
        print('动物吃肉...')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')

class Cat(Animal):
    def eat(self):
        print('猫吃老鼠...')

class People:
    def eat(self):
        print('人吃五谷杂粮...')

def fun(obj):
    obj.eat()

fun(People())
fun(Cat())
fun(Animal())