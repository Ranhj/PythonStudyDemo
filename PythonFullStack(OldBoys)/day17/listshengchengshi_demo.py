# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-13 10:00
# className:  listshengchengshi_demo.py
# 列表生成式
a = [x for x in range(10)]
print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a2 = [x*2 for x in range(10)]
print(a2)   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a3 = [x*x for x in range(10)]
print(a3)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



def f(n):
    return n ** 3

a4 = [f(x) for x in range(10)]
print(a4)   # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(type(a4)) # <class 'list'>

