# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 14:46
# IDE:        PyCharm
# Title:      func_duohanshuzhixingliucheng_demo2.py
# 多函数程序执行流程 -- 返回值作为参数传递
def test1():
    return 100

def test2(num):     # 定义形参  num
    print(num)

# 1.保存函数test1的返回值 到result变量
result = test1()
# 2.将函数返回值所在变量作为参数传递到test2函数
test2(result)   # 100