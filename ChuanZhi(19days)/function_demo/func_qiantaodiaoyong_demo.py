# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/10 17:08
# IDE:        PyCharm
# Title:      func_qiantaodiaoyong_demo.py
# 函数的嵌套调用
# 两个函数 testA 和 testB    --在A里面嵌套调用B
# 定义B函数
def testB():
    print('-'*5, 'B函数start', '-'*5)
    print('This is Func_B')
    print('-'*5, 'B函数end', '-'*5)

# 定义A函数
def testA():
    print('-'*5, 'A函数start', '-'*5)
    testB()
    print('-'*5, 'A函数end', '-'*5)

testA()