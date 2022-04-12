# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 15:25
# IDE:        PyCharm
# Title:      shezhihefangwenleishuxing_demo.py
# 设置和访问类属性
# 类属性就是 类对象 所拥有的属性，它被 该类的所有实例对象 所共有
# 类属性可以使用 类对象 或 实例对象 访问
"""
类属性的优点：
    记录的某些数据 始终保持一致时， 则定义类属性
    实例属性 要求 每个对象 为其 单独开辟一份内存空间 来记录数据，而 类属性 为全类所共有，仅占用一份内存，更加节省内存控件
"""
# 1.定义类，定义类属性
class Dog(object):
    tooth = 10

# 2.创建对象
xiaohei = Dog()
wangcai = Dog()

# 3.访问类属性： 用类和对象分别去访问
print(Dog.tooth)        # 10 类
print(xiaohei.tooth)    # 10 对象
print(wangcai.tooth)    # 10 对象