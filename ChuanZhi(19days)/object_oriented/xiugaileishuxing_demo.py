# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 15:42
# IDE:        PyCharm
# Title:      xiugaileishuxing_demo.py
# 修改类属性
class Dog(object):
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

# 1.通过类去修改类属性：  类.类属性 = 值
Dog.tooth = 20
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

# 2.测试通过对象修改类属性
wangcai.tooth = 15
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

