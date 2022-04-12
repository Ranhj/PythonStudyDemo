# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/19 14:17
# IDE:        PyCharm
# Title:      inheritance_demo.py
"""
python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法

拓展1： 经典类 或 旧式类
    不由任意内置类型派生出的类，称之为经典类

    class 类名：
        代码
        .....

拓展2：新式类  --主要学这个   括号里的object，是默认继承自object类， 子类继承父类时，括号里就不能写object，须写要继承的父类
    class 类名(object)
        代码
"""
# 在python中，所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类
# 继承：子类默认继承父类的所有属性和方法
# 1. 定义分类
class A():
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 2. 定义子类，继承父类
class B(A):
    pass

# 3. 创建对象，验证结论
result = B()
result.info_print()
