# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 16:28
# IDE:        PyCharm
# Title:      staticmethod_demo.py
"""
静态方法特点：
    需要通过装饰器@staticmethod 来进行修饰，静态方法既不需要传递类对象 也不需要传递实例对象（形参没有self/cls）
    静态方法 也能够通过 实例对象 和 类对象 去访问

静态方法使用场景：
    当方法中 既不需要使用实例对象（如实例对象，实例属性），也不需要使用类对象（如类属性、类方法、创建实例等）时，定义静态方法
    取消不需要的参数传递，有利于 减少不必要的内存占用和性能消耗
"""
# 1.定义类，定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个狗类，用于创建狗实例')
# 2.创建对象
xiaohei = Dog()
# 3.调用静态方法： 类 和 对象
# 静态方法既可以使用对象访问又可以使用类访问
xiaohei.info_print()
Dog.info_print()