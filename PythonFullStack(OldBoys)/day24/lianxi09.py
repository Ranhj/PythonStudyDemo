# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-09-28 15:48
# className:  lianxi09.py

class Foo:
    def __init__(self):
        self.name = 'aaa'
        # obj.name

    def bar(self):
        # self是对象
        print('bar')
    # 用于执行 obj.per
    @property
    def per(self):
        # print('123')
        return 1
    # obj.per = 123
    @per.setter
    def per(self, val):
        print(val)

    @per.deleter
    def per(self):
        print(666)


obj = Foo()
# # obj.per()
# # obj.per     # 伪造成通过字段去访问
# r = obj.per
# print(r)

obj.per = 123

del obj.per