# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/21 16:16
# IDE:        PyCharm
# Title:      classmethod_demo.py
# 类方法
# 需要用装饰器@classmethod来标识其为类方法
# 对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数

# 1.定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

# 2.创建对象，调用类方法
xiaohei = Dog()
result = xiaohei.get_tooth()
print(result)   # 10
