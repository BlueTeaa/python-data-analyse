# -*- codeing = utf-8 -*-
# @Time : 2023/9/6 11:28
# @Author : Yang
# @File : Lambda_map_filter_listComprehension.py
# @Software : PyCharm

def add(num1, num2):
    return num1 + num2


# lambda 是一个没有名的函数
abplus = lambda num1, num2: num1 + num2
a = abplus(10, 3)


# print(a)

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


even1 = lambda num: num % 2 == 0
# 冒号后是一个一行的表达式，参数可以有多个
b = even1(11)
# print(b)

def even_odd(num):
    if num%2==0:
        return 'the number {} is even'.format(num)
    else:
        return 'the number {} is odd'.format(num)

# print(even_odd(25))

# 判断列表中数据的奇偶性
lst = [1,2,8,5,6,3,4,7,8]
# for i in lst:
#     x = even_odd(i)
#     print(x)

#map
# map(function,lst) 一行解决for循环语句
# 返回return的信息
# print(list(map(even_odd,lst)))


# filter  函数+循环的单元值
# 返回判别条件为True的值
# print(list(filter(even,lst)))

# print(list(filter(lambda num:num%2==0,lst)))

print([i*2 for i in lst])
# 将for 和 if 结合起来使用
print([i*2 for i in lst if i%2==0])