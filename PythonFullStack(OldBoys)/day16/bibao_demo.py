# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-11 13:48
# className:  bibao_demo.py
# 闭包
def outer(x):
    # x = 10
    def inner():    # 条件一：inner就是内部函数
        print(x)    # 条件二：外部环境的一个变量

    return inner()  # 结论：内部函数inner就是一个闭包

outer(50)
# inner() # 这是局部变量，全局无法调用
# 关于闭包：闭包 = 内部函数 + 定义函数时的环境