# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 17:31
# IDE:        PyCharm
# Title:      func_qtdy_hanshujisuan_demo.py
# 1.任意三个数之和
def sum_num(a, b, c):
    return a + b + c

# result = sum_num(1, 2, 3)
# print(result)
# 2.任意三个数求平均值
def average_num(a, b, c):
    # 先求和，再除以3
    sumResult = sum_num(a, b, c)
    return sumResult / 3

averageResult = average_num(1, 2, 3)
print(averageResult)    # 2.0

