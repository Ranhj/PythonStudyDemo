# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 17:32
# IDE:        PyCharm
# className:  tuple_demo.py
# 元组特点：定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型
t1 = (1, 'A', '你好')
print(type(t1))     # <class 'tuple'>
t2 = (1,)
print(type(t2))     # <class 'tuple'>
# 注意：如果定义的元组只有一个数据，那么这个数据后面也要添加逗号，否则数据类型为唯一的这个数据的数据类型，就不再是tuple元组类型了
t3 = (1)
print(type(t3))     # <class 'int'>
t4 = ('Hello')
print(type(t4))     # <class 'str'>