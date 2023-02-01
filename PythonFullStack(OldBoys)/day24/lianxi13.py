# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-23 14:29
# className:  lianxi13.py
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "%s-%s"%(self.name, self.age)

obj = Foo('alex', 18)
func = getattr(obj, 'show')
print(func)
r = func()
print(r)

# # getattr 去什么东西里面获取什么内容
# inp = input('>>>')
# v = getattr(obj, inp)
# print(v)

# 通过字符串的形式操作对象中的成员
# getattr
# hasattr
# setattr
# delattr