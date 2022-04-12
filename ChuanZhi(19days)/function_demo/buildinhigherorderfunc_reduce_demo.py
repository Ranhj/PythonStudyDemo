# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 10:42
# IDE:        PyCharm
# Title:      buildinhigherorderfunc_reduce_demo.py
# 内置函数 reduce(func, lst)  其中func必须要有两个参数。
# 每次func计算的结果继续和序列的下一个元素做累积计算
list1 = [1, 2, 3, 4, 5, 6]
# 1.导入模块
import functools

# 2.定义功能函数  累积
def func(a, b):
    return a + b
# 2.1 累乘
def func2(a, b):
    return a * b

# 3.调用reduce， 作用：功能函数计算的结果和序列的下一个数据做累计计算
result = functools.reduce(func, list1)
print(result)   # 21
result2 = functools.reduce(func2, list1)
print(result2)  # 720
