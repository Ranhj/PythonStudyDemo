# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/15 14:06
# IDE:        PyCharm
# Title:      func_lambda_demo.py
# lambda表达式     lambda 参数列表： 表达式
# 需求： 函数 返回值100
# 1.函数实现
def fn1():
    return 100
print(fn1)      # <function fn1 at 0x01B460B8>
result = fn1()
print(result)   # 100

# 2.lambda  （匿名函数）
# lambda 参数列表： 表达式
fn2 = lambda: 100
print(fn2)      # lambda内存地址    <function <lambda> at 0x01B46070>
print(fn2())  # 100

# 直接打印lambda表达式，输出的是此lambda的内存地址
print(lambda: 200)  # <function <lambda> at 0x016C60B8>
