# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-23 15:59
# className:  lianxi16.py

class F1:

    def __init__(self):
        self.name = 123

class F2:

    def __init__(self, a):
        self.ff = a     # [name=123]

class F3:

    def __init__(self, b):
        self.dd = b

f1 = F1()       # [name=123]
f2 = F2(f1)     # [ff=[name=123]]
f3 = F3(f2)     # [dd=[ff=[name=123]]]
# 找到123并输出
print(f3.dd.ff.name)
