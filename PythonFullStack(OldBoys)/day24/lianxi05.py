# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-09-09 10:46
# className:  lianxi05.py
class F:
    def f1(self):
        print("F.f1")

    def f2(self):
        print("F.f2")

class S(F):
    def s1(self):
        print("S.s1")

    def s2(self):
        print("S.s2")
        # 调用父类的两种方法，推荐用super调用方法
        super(S, self).f2()  # 执行父类（基类）中的f2方法，推荐用这种方法
        F.f2(self)  # 直接调用，需要手动传self   执行父类（基类）中的f2方法

obj = S()
obj.s1()    # s1中的self是形参，此时代指 obj
obj.f1()    # self永远指调用方法的调用者
obj.s2()