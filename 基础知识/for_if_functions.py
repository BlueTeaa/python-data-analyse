# -*- codeing = utf-8 -*-
# @Time : 2023/9/5 20:17
# @Author : Yang
# @File : for_if_functions.py
# @Software : PyCharm

num = 24
def ji_or_ou(a):
    if a % 2 == 0:
        print('这是一个偶数')
    else:
        print("这是一个奇数")
    return a
x = ji_or_ou(num)
print(x)

def hello(name, age=24):
    print('My name is {} and age is {}'.format(name,age))

hello('Bob', 27)

def Hello(*args, **kargs):
    print(args)
    print(kargs)
Hello('Bob','chen',age=20,birthday=2000)
input_num = list(input("Enter the list   "))
print(input_num)