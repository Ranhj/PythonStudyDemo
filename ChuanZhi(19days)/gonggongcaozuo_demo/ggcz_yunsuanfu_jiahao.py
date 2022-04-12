# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 15:07
# IDE:        PyCharm
# className:  ggcz_yunsuanfu_jiahao.py
# 公共操作之运算符：+ 合并
str1 = 'abc'
str2 = 'def'

list1 = [1, 2, 3]
list2 = [10, 20, 30]

t1 = (1, 2, 3)
t2 = (10, 20, 30)

dict1 = {'name':'Jack'}
dict2 = {'hobby':'guitar'}

# + 合并
print(str1 + str2)              # abcdef
print(type(str1 + str2))        # <class 'str'>
print(list1 + list2)            # [1, 2, 3, 10, 20, 30]
print(type(list1 + list2))      # <class 'list'>
print(t1 + t2)                  # (1, 2, 3, 10, 20, 30)
print(type(t1 + t2))            # <class 'tuple'>
# print(dict1 + dict2)            # 报错：字典不支持合并运算  TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
