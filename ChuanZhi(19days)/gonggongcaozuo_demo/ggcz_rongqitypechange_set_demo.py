# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 10:54
# IDE:        PyCharm
# Title:      ggcz_rongqitypechange_set_demo.py
# set(): 转换成集合
list1 = [10, 50, 30, 50, 40, 60, 80]
t1 = ('a', 'b', 'c', 'd', 'e')
# list --> set: set有自动去重的效果，所以会自动去掉重复的数据，要注意！
set1 = set(list1)
print(type(set1))       # <class 'set'>
print(set1)             # {40, 10, 80, 50, 60, 30}
# tuple --> set:
set2 = set(t1)
print(type(set2))       # <class 'set'>
print(set2)             # {'e', 'c', 'd', 'b', 'a'}
