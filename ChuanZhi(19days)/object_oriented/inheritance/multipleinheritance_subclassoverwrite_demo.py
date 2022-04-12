# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/19 16:18
# IDE:        PyCharm
# Title:      multipleinheritance_subclassoverwrite_demo.py
# 子类重写父类同名属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 定义徒弟类，继承师傅类 和 学校类 ，添加和父类同名的属性和方法
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创煎饼]'
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

xiaoC = Prentice()
print(xiaoC.kongfu)
xiaoC.make_cake()
# 结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法

# 打印继承层级关系
"""
写法：
    (要查看的)类名.__mro__
"""
print(Prentice.__mro__)
# (<class '__main__.Prentice'>, <class '__main__.Master'>, <class '__main__.School'>, <class 'object'>)

print(Master.__mro__)
# (<class '__main__.Master'>, <class 'object'>)
