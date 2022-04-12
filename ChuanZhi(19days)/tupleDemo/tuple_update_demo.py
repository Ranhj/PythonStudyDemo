# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/7 9:37
# IDE:        PyCharm
# className:  tuple_update_demo.py
# tuple 元组不能直接修改，修改会报错；但是如果元组里面有列表，修改列表里面的数据则是可以的，故自觉很重要！！！
t1 = ('aa', 'bb', ['cc', 'dd'])
print(t1)               # ('aa', 'bb', ['cc', 'dd'])
# t1[0] = 'aaa'
# print(t1)               # 直接修改元组数据报错 TypeError: 'tuple' object does not support item assignment
print(t1[2][0])         # cc
t1[2][0] = 'ccccc'      # ('aa', 'bb', ['ccccc', 'dd'])
print(t1)
