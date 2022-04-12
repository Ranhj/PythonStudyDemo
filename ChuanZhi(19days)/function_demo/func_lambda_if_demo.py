# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/15 16:10
# IDE:        PyCharm
# Title:      func_lambda_if_demo.py
# 带判断的lambda  两个数字比大小   三目运算符
fn1 = lambda a, b: a if a > b else b
print(fn1(2, 3))    # 3
print(fn1(5, 3))    # 5
