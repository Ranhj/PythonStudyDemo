# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 9:48
# IDE:        PyCharm
# Title:      dict_comprehensions_merge_demo.py
# 如果两个列表数据个数相同，len统计任何一个列表的长度都可以
list1 = ['name', 'age', 'hobby']
list2 = ['Jack', 18, 'guitar']
# dict1 = {list1[i]: list2[i] for i in range(len(list1))}   # {'name': 'Jack', 'age': 18, 'hobby': 'guitar'}
dict1 = {list1[i]: list2[i] for i in range(len(list2))}     # {'name': 'Jack', 'age': 18, 'hobby': 'guitar'}
print(dict1)

# 如果两个列表数据个数不同，len统计数据多的列表数据个数会报错；len统计数据少的列表数据个数不会报错
list3 = ['name', 'age', 'hobby', 'gender']
list4 = ['Jack', 18, 'guitar']
# dict2 = {list3[i]: list4[i] for i in range(len(list3))}   # IndexError: list index out of range
dict2 = {list3[i]: list4[i] for i in range(len(list4))}     # {'name': 'Jack', 'age': 18, 'hobby': 'guitar'}
print(dict2)
