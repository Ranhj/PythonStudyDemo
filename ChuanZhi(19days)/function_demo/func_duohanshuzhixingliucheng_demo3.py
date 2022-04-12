# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 15:06
# IDE:        PyCharm
# Title:      func_duohanshuzhixingliucheng_demo3.py
# 如果一个函数有多个return，不能都执行，只执行第一个return就返回了，无法做到一个函数多个返回值
# def return_num():
#     return 1
#     return 2
#
# result = return_num()
# print(result)

# return a, b 写法，可以返回多个数据，返回的多个数据默认类型是元组类型

def return_num():
    # return后面可以连接列表、元组或字典，以返回多个值
    # return 1, 2           # (1, 2) 默认返回的是元组
    # return (10, 20)       # (10, 20)
    # return [100, 200]     # [100, 200]
    return {'name': 'Jack', 'hobby': 'guitar'}  # {'name': 'Jack', 'hobby': 'guitar'}
result = return_num()
print(result)
