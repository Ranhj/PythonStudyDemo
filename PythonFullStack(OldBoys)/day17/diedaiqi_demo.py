# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-16 17:01
# className:  diedaiqi_demo.py
# 生成器都是迭代器，迭代器不一定是生成器
# list, tuple, dict, string:Iterable (可迭代对象)
l = [1, 2, 3, 4]
d = iter(l)     # l.__iter__()
print(d)    # <list_iterator object at 0x000001D54CC39F40>

# # 什么是迭代器？ 满足两个条件：1.有iter方法  2.有next方法
# print(next(d))  # 1
# print(next(d))  # 2
# print(next(d))  # 3
# print(next(d))  # 4
# # print(next(d))  # StopIteration
#
# # for 循环内部三件事：
# # 1.调用可迭代对象的iter方法返回一个迭代器对象
# # 2.不断调用迭代器对象的next方法
# # 3.处理StopIteration异常
# for i in [1, 2, 3, 4]:
#     iter([1, 2, 3, 4])

from collections import Iterator,Iterable
print(isinstance(l, list))  # True
print(isinstance(l, Iterable))  # True
print(isinstance(l, Iterator))  # False
print(isinstance(d, Iterator))  # True

'''
需要明确的就是生成器也是iterator迭代器，因为它遵循了迭代器协议
两种创建方式
包含yield的函数
生成器函数跟普通函数只有一点不一样，就是把return换成yield，其中yield是一个语法糖，内部实现了迭代器协议，同时保持状态可以挂起
'''