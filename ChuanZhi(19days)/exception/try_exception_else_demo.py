# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/22 10:51
# IDE:        PyCharm
# Title:      try_exception_else_demo.py
# else 表示的是如果没有异常要执行的代码
"""
try:
    可能出现异常的代码
except:
    出现异常时执行的代码
else:
    没有异常时执行的代码
"""
try:
    print(2/3)
except Exception as result:
    print(result)
else:
    print('我是else，当没有异常时执行的代码')