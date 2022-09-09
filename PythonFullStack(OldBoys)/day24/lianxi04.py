# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-09-09 10:29
# className:  lianxi04.py
class GrandFather:  # 父类，也叫基类
    def pingpang(self):
        print("会打乒乓球")

class Father(GrandFather):  # 子类，也叫派生类
    def basketball(self):
        print("会打篮球")

class Son(Father):
    def football(self):
        print("会踢足球")

x = Son()
x.football()
x.basketball()
x.pingpang()
