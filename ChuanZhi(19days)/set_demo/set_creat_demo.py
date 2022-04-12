# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 9:48
# IDE:        PyCharm
# className:  set_creat_demo.py
#  1.创建有数据的集合
# 打印集合，不会按照默认输入的排序来打印，因为集合内是没有下标的
s1 = {10, 20, 30, 40, 50, 60, 70, 80, 90}       # {70, 40, 10, 80, 50, 20, 90, 60, 30}
print(s1)
# 集合内的数据会自动去重
s2 = {10, 20, 30, 20, 30, 40}                   # {40, 10, 20, 30}
print(s2)
# set() set创建的集合内的字符串会默认输出子串的形式，也不会按照输入的排序打印
s3 = set('abcdef')                              # {'b', 'c', 'd', 'f', 'e', 'a'}
print(s3)

# 创建无数据的集合 set()
# 创建空集合，必须使用set()的形式，否则创建的类型就字典！！！
s4 = set()
print(s4)           # set()
print(type(s4))     # <class 'set'> 类型：集合

s5 = {}
print(s5)           # {}
print(type(s5))     # <class 'dict'> 类型：字典

