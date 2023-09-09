# -*- codeing = utf-8 -*-
# @Time : 2023/9/7 8:56
# @Author : Yang
# @File : classes_variable.py
# @Software : PyCharm

class Student:
    pass

xiaoming = Student()
xiaoming.age = 10
xiaoming.grade = 4

class Car:
    def __init__(self, window, door, engine):
        self.window = window
        self.door = door
        self.engine = engine

    def info(self, brand):
        self.brand = brand

    def printInfo(self):
        return "This is a {x} {y} car".format(x=self.engine, y=self.brand)
car2 = Car(4,4,'4 cylinder')
car2.brand = "Audi"

print(car2.printInfo())


