# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 14:20
# IDE:        PyCharm
# Title:      func_duohanshuzhixingliucheng_demo.py
# 多函数执行流程   --  共用全局变量
"""
1.声明全局变量
2.定义两个函数
3.函数一 修改全局变量，函数二访问全局变量
"""
glo_num = 0

def test1():
    global glo_num
    glo_num = 100

def test2():
    print(glo_num)

print(glo_num)      # 0
test2()             # 0 修改的函数还没调用执行，所以这个时候还是0
test1()
test2()             # 100 先调用了函数1，执行了赋值100的操作，所以是100
print(glo_num)      # 100 调用了函数1