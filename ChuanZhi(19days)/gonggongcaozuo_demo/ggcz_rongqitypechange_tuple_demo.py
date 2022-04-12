# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/9 10:44
# IDE:        PyCharm
# Title:      ggcz_rongqitypechange_tuple_demo.py

# tuple(): 转换成元组
list1 = [10, 50, 30, 40, 60, 80]
s1 = {200, 100, 300, 500, 400}

# list --> tuple
tuple1 = tuple(list1)
print(type(tuple1))     # <class 'tuple'>
print(tuple1)           # (10, 50, 30, 40, 60, 80)
# list --> tuple
tuple2 = tuple(s1)
print(type(tuple2))     # <class 'tuple'>
print(tuple(s1))        # (100, 200, 300, 400, 500)
