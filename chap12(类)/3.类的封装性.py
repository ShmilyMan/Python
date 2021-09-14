# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 17:19
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 3.类的封装性.py
# @Software: PyCharm

class Car:

    def __init__(self,carName):
        self.__carName = carName # 如果希望一个类中的对属性不希望被外界使用，在属性前面加上__

    def get_carName(self):
        return self.__carName

    def set_carName(self,carName):
        self.__carName = carName


car = Car('奔驰')
# 此时不能在类的外部调用他的carName属性，但可以使用以下方法调用（基本不用）
print(dir(car))
print(car._Car__carName) # 奔驰  _类名__属性名

