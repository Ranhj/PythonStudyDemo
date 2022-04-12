# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/22 10:18
# IDE:        PyCharm
# Title:      catchingSpecifiedException_demo.py
# 捕获指定异常
"""
语法：
try:
    可能发生错误的代码
except 异常类型：
    如果捕获到该异常类型执行的代码
"""
# 需求：尝试执行打印num，捕获异常类型NameError，如果捕获到这个异常类型，执行打印：有错误
# 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
# 一般try下方只放一行尝试执行的代码
try:
    print(num)
except NameError:
    print('有错误')  # 有错误

# try:
#     print(1/0)
# except NameError:
#     print('有错误')    # 报错：ZeroDivisionError: division by zero

# 捕获多个指定异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('有错误')  # 有错误

# 捕获异常描述信息
try:
    print(1/0)
except(NameError, ZeroDivisionError) as result:
    print(result)   # division by zero

# 捕获所有异常
# Exception是所有程序异常类的父类
try:
    print(1/0)      # division by zero
    # print(num)      # name 'num' is not defined
except Exception as result:
    print(result)