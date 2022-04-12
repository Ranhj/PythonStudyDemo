# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 10:42
# IDE:        PyCharm
# Title:      func_localvariable_demo.py
# 局部变量的作用：
#     在函数体内部，临时报错数据，即当函数调用完成以后，则销毁局部变量
# 所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
# 定义一个函数，声明一个变量：    测试函数体内部访问、函数体外面访问
def testA():
    a = 100
    print(a)

testA()     # 100
# print(a)    # 报错： a 变量是函数内部的变量，函数外部无法访问，a 变量是一个局部变量  NameError: name 'a' is not defined