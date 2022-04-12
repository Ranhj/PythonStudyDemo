# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 10:16
# IDE:        PyCharm
# Title:      publicmethod_enumerate_demo.py
# enumerate(可遍历对象，start=0) 返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
str1 = 'abcdef'
list1 = [1, 2, 3, 4, 5]
t1 = (10, 20, 30, 40, 50)
s1 = {100, 200, 300, 400, 500}
dict1 = {'name': 'Tom', 'hobby': 'guitar'}

print('-'*5, 'enumerate_str1', '-'*5)
for i in enumerate(str1, start=0):  # start=0 省略不写则默认start为0
    print(i)

print('-'*5, 'enumerate_str1', '-'*5)
for index, char in enumerate(str1, start=1):  # start=1 start为1打印的时候下标就会从1开始排
    print(f'返回的下标是{index},字符是{char}')

print('-' * 5, 'enumerate_list1', '-' * 5)
for i in enumerate(list1):
    print(i)

print('-' * 5, 'enumerate_t1', '-' * 5)
for i in enumerate(t1):
    print(i)

print('-' * 5, 'enumerate_s1', '-' * 5)
for i in enumerate(s1):
    print(i)

print('-' * 5, 'enumerate_dict1', '-' * 5)
for i in enumerate(dict1):
    print(i)