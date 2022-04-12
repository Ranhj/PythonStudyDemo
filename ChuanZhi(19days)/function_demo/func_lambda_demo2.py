# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/15 15:18
# IDE:        PyCharm
# Title:      func_lambda_demo2.py
# 需求：计算任意两个数字的累加和
# 1.函数
def add(a, b):
    return a + b
result = add(1, 2)
print(result)   # 3

# 2.lambda
fn1 = lambda a, b: a + b
print(fn1(2, 3))    # 5
