# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 10:55
# IDE:        PyCharm
# Title:      buildinhigherorderfunc_filter_demo.py

# filter(func, lst)函数   用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象
# 如果要转换为列表，可以使用list()来转换
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.定义功能函数：过滤序列中的偶数
def func(x):
    return x % 2 == 0

# 1.1 定义功能函数：过滤序列中的基数
def func2(x):
    return x % 2 == 1

# 2.调用filter
result = filter(func, list1)
print(list(result))     # [2, 4, 6, 8, 10]

result2 = filter(func2, list1)
print(list(result2))    # [1, 3, 5, 7, 9]