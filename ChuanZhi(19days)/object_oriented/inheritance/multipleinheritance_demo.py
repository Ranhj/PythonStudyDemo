# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/19 15:51
# IDE:        PyCharm
# Title:      multipleinheritance_demo.py
# 多继承   意思就是一个类同时继承了多个父类
# 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
# 定义第一个父类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 定义第二个父类
class HeiMa(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼]'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 定义徒弟类，继承两个父类
class Prentice(HeiMa, Master):
    pass

# 实测，子类只继承了第一个传入的父类
xiaoA = Prentice()
print(xiaoA.kongfu)
xiaoA.make_cake()
# 结论：如果一个类继承多个父类，优先继承第一个父类的同名属性和方法
