# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/15 9:46
# IDE:        PyCharm
# Title:      func_recursion_demo.py
# 递归特点：函数内部自己调用自己；  必须有出口
# 函数返回值 返回的位置：函数调用的位置
# 3 + 2 + 1
def sum_numbers(num):
    # 1.如果是1，直接返回1  --出口
    # 如果没有出口会报错：超出最大递归深度  [Previous line repeated 996 more times]  RecursionError: maximum recursion depth exceeded
    if num == 1:
        return 1
    # 2.如果不是1，重复执行累加并返回结果
    return num + sum_numbers(num-1)

sum_result = sum_numbers(3)
print(sum_result)   # 6