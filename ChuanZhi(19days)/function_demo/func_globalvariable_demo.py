# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 11:06
# IDE:        PyCharm
# Title:      func_globalvariable_demo.py
# 全局变量：所谓全局变量，指的是在函数体内、外部都能生效的变量
# 定义全局变量a
a = 100
def testA():
    print(a)    # 访问全局变量a，并打印变量a存储的数据

def testB():
    print(a)    # 访问全局变量a，并打印变量a存储的数据

testA()     # 100
testB()     # 100
