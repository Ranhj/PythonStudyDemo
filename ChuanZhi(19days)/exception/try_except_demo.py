# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 17:19
# IDE:        PyCharm
# Title:      try_except_demo.py
# 异常
# 需求 ： 尝试打开test.txt(r), 如果文件不存在，只写方式打开(w)
"""
try:
    可能发送错误的代码
except:
    发送错误的时候执行的代码
"""
try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')