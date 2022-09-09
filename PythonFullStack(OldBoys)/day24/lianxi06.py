# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-09-09 14:27
# className:  lianxi06.py
# python支持多继承，左侧优先
class A:
    def a(self):
        print("A.a")

class B:
    def b(self):
        # print("B.b")
        self.b1()

    def b1(self):
        print("B.b1")

class C(A, B):  # 左侧A优先，找不到的时候再去右侧B找
    def c(self):
        print("C.c")

obj = C()
obj.b()     # B.b1