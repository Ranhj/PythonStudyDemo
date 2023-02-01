# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-09-28 15:20
# className:  lianxi08.py
# 静态方法和普通方法的区别：
# 1.有装饰器@staticmethod
# 2.方法中的self就不是必须的了
# 3.可以直接用类名去调用方法

class Foo:
    def bar(self):
        # self 是对象
        print('bar')

    @staticmethod   # 静态方法
    def sta():  # 静态方法，括号中的self就不是必须的了
        print('123')

    @staticmethod
    def stat(a1, a2):
        print(a1, a2)

    @classmethod
    def classmd(cls):
        # cls 是类名
        print(cls)  # <class '__main__.Foo'>
        print('classmd')

obj = Foo()
obj.bar()

obj.sta()

Foo.stat(1, 2)  # 用类直接调用方法

Foo.classmd()