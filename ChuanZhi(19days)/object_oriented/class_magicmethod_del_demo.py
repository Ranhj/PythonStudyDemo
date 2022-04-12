# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/18 16:12
# IDE:        PyCharm
# Title:      class_magicmethod_del_demo.py
# __del__()
# 当删除对象时，python解释器也会默认调用__del__()方法
class Washer():
    def __init__(self):
        self.width = 300

    def __del__(self):
        print(f'{self}对象已被删除！')     # 执行完所有的代码之后，内存会自动删除类、函数、变量等之类的

haier = Washer()
