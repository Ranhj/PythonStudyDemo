# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 15:23
# IDE:        PyCharm
# Title:      functiondemo2.py
def add_num():
    result = 1 + 2
    print(result)

add_num()   # 3

# 参数形式传入真实数据
def add_num2(a, b):     # a, b：形参
    result = a + b
    print(result)

add_num2(10, 30)        # 40        10，30：实参
# add_num2(10)    # 报错！定义函数有2个参数，传入数据也要是2个 TypeError: add_num2() missing 1 required positional argument: 'b'