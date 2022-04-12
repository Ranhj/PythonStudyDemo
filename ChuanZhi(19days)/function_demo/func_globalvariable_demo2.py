# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/11 14:04
# IDE:        PyCharm
# Title:      func_globalvariable_demo2.py
# B函数想要a的取值是200
a = 100
print(a)    # 100

def testA():
    print(a)

def testB():
    # a = 200 # 如果直接修改a=200，此时的a是全局a还是局部a？ --得到结论：这个a是局部变量
    # # 因为在全局位置(B函数调用后)打印a得到的不是200而是100
    # print(a)

    # 想要修改全局变量a,值是200
    global a    # 声明a为全局变量
    a = 200
    print(a)

testA()     # 100
testB()     # 200
print(a)    # 200
"""
总结：
    1.如果在函数里面直接把变量a=200赋值，此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
    2.函数体内部修改全局变量，先global声明a为全局变量，然后再变量重新赋值
"""