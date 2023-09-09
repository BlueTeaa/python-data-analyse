# -*- codeing = utf-8 -*-
# @Time : 2023/9/6 11:59
# @Author : Yang
# @File : string_iterablesvslterators_pyforest.py
# @Software : PyCharm

lst = [1,2,3,4,5,6,7,8,9]
lst2 = iter(lst)
next(lst2)
for i in lst2:
    print(i)

#iter 分配地址空间，通过next方式，减少内存占用
